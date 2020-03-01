/*************************************************************************
 Copyright (C) 2008 by Bruno Chareyre		                         *
*  bruno.chareyre@hmg.inpg.fr      					 *
*                                                                        *
*  This program is free software; it is licensed under the terms of the  *
*  GNU General Public License v2 or later. See file LICENSE for details. *
*************************************************************************/
#include<sudodem/lib/base/Math.hpp>
#include<sudodem/pkg/dem/NewtonIntegrator.hpp>
#include<sudodem/core/Scene.hpp>
#include<sudodem/core/Clump.hpp>
//#include<sudodem/lib/base/Math.hpp>


SUDODEM_PLUGIN((NewtonIntegrator));
CREATE_LOGGER(NewtonIntegrator);

// 1st order numerical damping
void NewtonIntegrator::cundallDamp1st(Vector3r& force, const Vector3r& vel){
	for(int i=0; i<3; i++) force[i]*=1-damping*Mathr::Sign(force[i]*vel[i]);
}
// 2nd order numerical damping
void NewtonIntegrator::cundallDamp2nd(const Real& dt, const Vector3r& vel, Vector3r& accel){
	for(int i=0; i<3; i++) accel[i]*= 1 - damping*Mathr::Sign ( accel[i]*(vel[i] + 0.5*dt*accel[i]) );
}

Vector3r NewtonIntegrator::computeAccel(const Vector3r& force, const Real& mass, int blockedDOFs){
	if(blockedDOFs==0) return (force/mass + gravity);
	Vector3r ret(Vector3r::Zero());
	for(int i=0; i<3; i++) if(!(blockedDOFs & State::axisDOF(i,false))) ret[i]+=force[i]/mass+gravity[i];
	return ret;
}
Vector3r NewtonIntegrator::computeAngAccel(const Vector3r& torque, const Vector3r& inertia, int blockedDOFs){
	if(blockedDOFs==0) return torque.cwiseQuotient(inertia);
	Vector3r ret(Vector3r::Zero());
	for(int i=0; i<3; i++) if(!(blockedDOFs & State::axisDOF(i,true))) ret[i]+=torque[i]/inertia[i];
	return ret;
}

void NewtonIntegrator::updateEnergy(const shared_ptr<Body>& b, const State* state, const Vector3r& fluctVel, const Vector3r& f, const Vector3r& m){
	assert(b->isStandalone() || b->isClump());
	// always positive dissipation, by-component: |F_i|*|v_i|*damping*dt (|T_i|*|ω_i|*damping*dt for rotations)
	if(damping!=0. && state->isDamped){
		scene->energy->add(fluctVel.cwiseAbs().dot(f.cwiseAbs())*damping*scene->dt,"nonviscDamp",nonviscDampIx,/*non-incremental*/false);
		// when the aspherical integrator is used, torque is damped instead of ang acceleration; this code is only approximate
		scene->energy->add(state->angVel.cwiseAbs().dot(m.cwiseAbs())*damping*scene->dt,"nonviscDamp",nonviscDampIx,false);
	}
	// kinetic energy
	Real Etrans=.5*state->mass*fluctVel.squaredNorm();
	Real Erot;
	// rotational terms
	if(b->isAspherical()){
		Matrix3r mI; mI<<state->inertia[0],0,0, 0,state->inertia[1],0, 0,0,state->inertia[2];
		Matrix3r T(state->ori);
		Erot=.5*b->state->angVel.transpose().dot((T.transpose()*mI*T)*b->state->angVel);
	} else { Erot=0.5*state->angVel.dot(state->inertia.cwiseProduct(state->angVel)); }
	if(!kinSplit) scene->energy->add(Etrans+Erot,"kinetic",kinEnergyIx,/*non-incremental*/true);
	else{ scene->energy->add(Etrans,"kinTrans",kinEnergyTransIx,true); scene->energy->add(Erot,"kinRot",kinEnergyRotIx,true); }
	// gravitational work (work done by gravity is "negative", since the energy appears in the system from outside)
	scene->energy->add(-gravity.dot(b->state->vel)*b->state->mass*scene->dt,"gravWork",fieldWorkIx,/*non-incremental*/false);
}

void NewtonIntegrator::saveMaximaVelocity(const Body::id_t& id, State* state){
	#ifdef SUDODEM_OPENMP
		Real& thrMaxVSq=threadMaxVelocitySq[omp_get_thread_num()]; thrMaxVSq=max(thrMaxVSq,state->vel.squaredNorm());
	#else
		maxVelocitySq=max(maxVelocitySq,state->vel.squaredNorm());
	#endif
}


void NewtonIntegrator::saveMaximaDisplacement(const shared_ptr<Body>& b){
	if (!b->bound) return;//clumps for instance, have no bounds, hence not saved
	Vector3r disp=b->state->pos-b->bound->refPos;
	Real maxDisp=max(std::abs(disp[0]),max(std::abs(disp[1]),std::abs(disp[2])));
	if (!maxDisp || maxDisp<b->bound->sweepLength) {/*b->bound->isBounding = (updatingDispFactor>0 && (updatingDispFactor*maxDisp)<b->bound->sweepLength);*/
	maxDisp=0.5;//not 0, else it will be seen as "not updated" by the collider, but less than 1 means no colliding
	}
	else {/*b->bound->isBounding = false;*/ maxDisp=2;/*2 is more than 1, enough to trigger collider*/}
	#ifdef SUDODEM_OPENMP
		Real& thrMaxVSq=threadMaxVelocitySq[omp_get_thread_num()]; thrMaxVSq=max(thrMaxVSq,maxDisp);
	#else
		maxVelocitySq=max(maxVelocitySq,maxDisp);
	#endif
}

#ifdef SUDODEM_OPENMP
void NewtonIntegrator::ensureSync()
{
	if (syncEnsured) return;
	SUDODEM_PARALLEL_FOREACH_BODY_BEGIN(const shared_ptr<Body>& b, scene->bodies){
// 		if(b->isClump()) continue;
		scene->forces.addForce(b->getId(),Vector3r(0,0,0));
	} SUDODEM_PARALLEL_FOREACH_BODY_END();
	syncEnsured=true;
}
#endif

void NewtonIntegrator::action()
{
	#ifdef SUDODEM_OPENMP
	//prevent https://bugs.launchpad.net/sudodem/+bug/923929
	ensureSync();
	#endif

	scene->forces.sync();
	bodySelected=(scene->selectedBody>=0);
	if(warnNoForceReset && scene->forces.lastReset<scene->iter) LOG_WARN("O.forces last reset in step "<<scene->forces.lastReset<<", while the current step is "<<scene->iter<<". Did you forget to include ForceResetter in O.engines?");
	const Real& dt=scene->dt;
	//Take care of user's request to change velGrad. Safe to change it here after the interaction loop.
	if (scene->cell->velGradChanged || scene->cell->nextVelGrad!=Matrix3r::Zero()) {
		scene->cell->velGrad=scene->cell->nextVelGrad;
		scene->cell->velGradChanged=0; scene->cell->nextVelGrad=Matrix3r::Zero();}
	homoDeform=scene->cell->homoDeform;
	dVelGrad=scene->cell->velGrad-prevVelGrad;
	// account for motion of the periodic boundary, if we remember its last position
	// its velocity will count as max velocity of bodies
	// otherwise the collider might not run if only the cell were changing without any particle motion
	// FIXME: will not work for pure shear transformation, which does not change Cell::getSize()
	if(scene->isPeriodic && ((prevCellSize!=scene->cell->getSize())) && /* initial value */!isnan(prevCellSize[0]) ){ cellChanged=true; maxVelocitySq=(prevCellSize-scene->cell->getSize()).squaredNorm()/pow(dt,2); }
	else { maxVelocitySq=0; cellChanged=false; }

	#ifdef SUDODEM_BODY_CALLBACK
		// setup callbacks
		vector<BodyCallback::FuncPtr> callbackPtrs;
		FOREACH(const shared_ptr<BodyCallback>& cb, callbacks){
			cerr<<"<cb="<<cb.get()<<", setting cb->scene="<<scene<<">";
			cb->scene=scene;
			callbackPtrs.push_back(cb->stepInit());
		}
		assert(callbackPtrs.size()==callbacks.size());
		size_t callbacksSize=callbacks.size();
	#endif

	const bool trackEnergy(scene->trackEnergy);
	const bool isPeriodic(scene->isPeriodic);

	#ifdef SUDODEM_OPENMP
		FOREACH(Real& thrMaxVSq, threadMaxVelocitySq) { thrMaxVSq=0; }
	#endif
	SUDODEM_PARALLEL_FOREACH_BODY_BEGIN(const shared_ptr<Body>& b, scene->bodies){
			// clump members are handled inside clumps
            if (b->shape->getClassName()=="TriElement") continue;
			if(b->isClumpMember()) continue;
			State* state=b->state.get(); const Body::id_t& id=b->getId();
			Vector3r f=Vector3r::Zero();
			Vector3r m=Vector3r::Zero();

			// clumps forces
			if(b->isClump()) {
				b->shape->cast<Clump>().addForceTorqueFromMembers(state,scene,f,m);
				#ifdef SUDODEM_OPENMP
				//it is safe here, since only one thread is adding forces/torques
				scene->forces.addTorqueUnsynced(id,m);
				scene->forces.addForceUnsynced(id,f);
				#else
				scene->forces.addTorque(id,m);
				scene->forces.addForce(id,f);
				#endif
			}
			//in most cases, the initial force on clumps will be zero and next line is not changing f and m, but make sure we don't miss something (e.g. user defined forces on clumps)
			f=scene->forces.getForce(id); m=scene->forces.getTorque(id);
			#ifdef SUDODEM_DEBUG
				if(isnan(f[0])||isnan(f[1])||isnan(f[2])) throw runtime_error(("NewtonIntegrator: NaN force acting on #"+boost::lexical_cast<string>(id)+".").c_str());
				if(isnan(m[0])||isnan(m[1])||isnan(m[2])) throw runtime_error(("NewtonIntegrator: NaN torque acting on #"+boost::lexical_cast<string>(id)+".").c_str());
				if(state->mass<=0 && ((state->blockedDOFs & State::DOF_XYZ) != State::DOF_XYZ)) throw runtime_error(("NewtonIntegrator: #"+boost::lexical_cast<string>(id)+" has some linear accelerations enabled, but State::mass is non-positive."));
				if(state->inertia.minCoeff()<=0 && ((state->blockedDOFs & State::DOF_RXRYRZ) != State::DOF_RXRYRZ)) throw runtime_error(("NewtonIntegrator: #"+boost::lexical_cast<string>(id)+" has some angular accelerations enabled, but State::inertia contains non-positive terms."));
			#endif

			// fluctuation velocity does not contain meanfield velocity in periodic boundaries
			// in aperiodic boundaries, it is equal to absolute velocity
			Vector3r fluctVel=isPeriodic?scene->cell->bodyFluctuationVel(b->state->pos,b->state->vel,prevVelGrad):state->vel;

			// numerical damping & kinetic energy
			if(trackEnergy) updateEnergy(b,state,fluctVel,f,m);

			// whether to use aspherical rotation integration for this body; for no accelerations, spherical integrator is "exact" (and faster)
			bool useAspherical=(exactAsphericalRot && b->isAspherical() && state->blockedDOFs!=State::DOF_ALL);

			// for particles not totally blocked, compute accelerations; otherwise, the computations would be useless
			if (state->blockedDOFs!=State::DOF_ALL) {
				// linear acceleration
				Vector3r linAccel=computeAccel(f,state->mass,state->blockedDOFs);
				if (densityScaling) linAccel*=state->densityScaling;
				if(state->isDamped) cundallDamp2nd(dt,fluctVel,linAccel);
				//This is the convective term, appearing in the time derivation of Cundall/Thornton expression (dx/dt=velGrad*pos -> d²x/dt²=dvelGrad/dt*pos+velGrad*vel), negligible in many cases but not for high speed large deformations (gaz or turbulent flow).
				if (isPeriodic && homoDeform) linAccel+=prevVelGrad*state->vel;
				//finally update velocity
				state->vel+=dt*linAccel;
				// angular acceleration
				//cout<<"useAs="<<useAspherical<<endl;
				if(!useAspherical){ // uses angular velocity
					Vector3r angAccel=computeAngAccel(m,state->inertia,state->blockedDOFs);
					if (densityScaling) angAccel*=state->densityScaling;
					if(state->isDamped) cundallDamp2nd(dt,state->angVel,angAccel);
					state->angVel+=dt*angAccel;
				} else { // uses torque
					for(int i=0; i<3; i++) if(state->blockedDOFs & State::axisDOF(i,true)) m[i]=0; // block DOFs here
					if(state->isDamped){ //zhswee
            if(isSuperquadrics){
								bool isSphere = false;
								switch (isSuperquadrics) {
									case 1:
									{
										Superquadrics* A = static_cast<Superquadrics*>(b->shape.get());
										isSphere = A->isSphere;
										break;
									}
									case 2:
									{
										PolySuperellipsoid* B = static_cast<PolySuperellipsoid*>(b->shape.get());
										isSphere = B->isSphere;
										break;
									}
									case 4:
									{
										GJKParticle* C = static_cast<GJKParticle*>(b->shape.get());
										isSphere = C->isSphere;
										break;
									}
									//default:
								}


                if (isSphere){

                    Vector3r angAccel=computeAngAccel(m,state->inertia,state->blockedDOFs);
                    cundallDamp2nd(dt,state->angVel,angAccel);
                    state->angVel+=dt*angAccel;
                    //std::cerr<<"angvel"<<(state->angVel)[1]<<"angA"<<angAccel[1]<<std::endl;
                }else{
                    cundallDamp1st(m,state->angVel);
                }
            }else{
  						cundallDamp1st(m,state->angVel);
            }
					//for(int i=0; i<3; i++) m[i]*=1-0.9*Mathr::Sign(m[i]*state->angVel[i]);

					}

				}
			// reflect macro-deformation even for non-dynamic bodies
			} else if (isPeriodic && homoDeform) state->vel+=dt*prevVelGrad*state->vel;

			// update positions from velocities (or torque, for the aspherical integrator)
			//check quiet_system_flag
            if (quiet_system_flag){//the flag is set to true from the other implementation
                state->vel = Vector3r::Zero();
                state->angVel = Vector3r::Zero();
            }
            else{//execute the normal script
			    if(!useAspherical) {leapfrogSphericalRotate(state,id,dt);}//zhswee
			    else if (isSuperquadrics){
						bool isSphere = false;
						switch (isSuperquadrics) {
							case 1:
							{
								Superquadrics* A = static_cast<Superquadrics*>(b->shape.get());
								isSphere = A->isSphere;
								if(!isSphere)leapfrogSuperquadricsRotate(A,state,id,dt,m);
								break;
							}
							case 2:
							{
								PolySuperellipsoid* B = static_cast<PolySuperellipsoid*>(b->shape.get());
								isSphere = B->isSphere;
								if(!isSphere)leapfrogPolySuperellipsoidRotate(B,state,id,dt,m);
								break;
							}
							case 4:
							{
								GJKParticle* C = static_cast<GJKParticle*>(b->shape.get());
								isSphere = C->isSphere;
								if(!isSphere)leapfrogGJKParticleRotate(C,state,id,dt,m);
								break;
							}
							//default:
						}

			       if (isSphere){leapfrogSphericalRotate(state,id,dt);}
			    }
			    else{
			            leapfrogAsphericalRotate(state,id,dt,m);
			         }
                leapfrogTranslate(state,id,dt);
            }
			saveMaximaDisplacement(b);
			// move individual members of the clump, save maxima velocity (for collider stride)
			if(b->isClump()) Clump::moveMembers(b,scene,this);

			#ifdef SUDODEM_BODY_CALLBACK
				// process callbacks
				for(size_t i=0; i<callbacksSize; i++){
					cerr<<"<"<<b->id<<",cb="<<callbacks[i]<<",scene="<<callbacks[i]->scene<<">"; // <<",force="<<callbacks[i]->scene->forces.getForce(b->id)<<">";
					if(callbackPtrs[i]!=NULL) (*(callbackPtrs[i]))(callbacks[i].get(),b.get());
				}
			#endif
	} SUDODEM_PARALLEL_FOREACH_BODY_END();
	if (quiet_system_flag){quiet_system_flag = false;}
	#ifdef SUDODEM_OPENMP
		FOREACH(const Real& thrMaxVSq, threadMaxVelocitySq) { maxVelocitySq=max(maxVelocitySq,thrMaxVSq); }
	#endif
	if(scene->isPeriodic) { prevCellSize=scene->cell->getSize(); prevVelGrad=scene->cell->prevVelGrad=scene->cell->velGrad; }
}

void NewtonIntegrator::leapfrogTranslate(State* state, const Body::id_t& id, const Real& dt){
	if (scene->forces.getMoveRotUsed()) state->pos+=scene->forces.getMove(id);
	// update velocity reflecting changes in the macroscopic velocity field, making the problem homothetic.
	//NOTE : if the velocity is updated before moving the body, it means the current velGrad (i.e. before integration in cell->integrateAndUpdate) will be effective for the current time-step. Is it correct? If not, this velocity update can be moved just after "state->pos += state->vel*dt", meaning the current velocity impulse will be applied at next iteration, after the contact law. (All this assuming the ordering is resetForces->integrateAndUpdate->contactLaw->PeriCompressor->NewtonsLaw. Any other might fool us.)
	//NOTE : dVel defined without wraping the coordinates means bodies out of the (0,0,0) period can move realy fast. It has to be compensated properly in the definition of relative velocities (see Ig2 functors and contact laws).
		//Reflect mean-field (periodic cell) acceleration in the velocity
	if(scene->isPeriodic && homoDeform) {Vector3r dVel=dVelGrad*state->pos; state->vel+=dVel;}

	if ( (mask<=0) or ((mask>0) and (Body::byId(id)->maskCompatible(mask))) ) {
		state->pos+=state->vel*dt;
	}
}

void NewtonIntegrator::leapfrogSphericalRotate(State* state, const Body::id_t& id, const Real& dt )
{
	Real angle2=state->angVel.squaredNorm();
	if (angle2!=0 and ( (mask<=0) or ((mask>0) and (Body::byId(id)->maskCompatible(mask))) )) {//If we have an angular velocity, we make a rotation
		Real angle=sqrt(angle2);
		Quaternionr q(AngleAxisr(angle*dt,state->angVel/angle));
		state->ori = q*state->ori;
	}
	if(scene->forces.getMoveRotUsed() && scene->forces.getRot(id)!=Vector3r::Zero()
		and ( (mask<=0) or ((mask>0) and (Body::byId(id)->maskCompatible(mask))) )) {
		Vector3r r(scene->forces.getRot(id));
		Real norm=r.norm(); r/=norm;
		Quaternionr q(AngleAxisr(norm,r));
		state->ori=q*state->ori;
	}
	state->ori.normalize();
}

void NewtonIntegrator::leapfrogAsphericalRotate(State* state, Matrix3r& A, const Body::id_t& id, const Real& dt, const Vector3r& M){
	//Matrix A: rotation matrix from global to local r.f.
	const Vector3r l_n = state->angMom + dt/2. * M; // global angular momentum at time n
	const Vector3r l_b_n = A*l_n; // local angular momentum at time n
	Vector3r angVel_b_n = l_b_n.cwiseQuotient(state->inertia); // local angular velocity at time n
	if (densityScaling) angVel_b_n*=state->densityScaling;
	const Quaternionr dotQ_n=DotQ(angVel_b_n,state->ori); // dQ/dt at time n
	const Quaternionr Q_half = state->ori + dt/2. * dotQ_n; // Q at time n+1/2
	state->angMom+=dt*M; // global angular momentum at time n+1/2
	const Vector3r l_b_half = A*state->angMom; // local angular momentum at time n+1/2
	Vector3r angVel_b_half = l_b_half.cwiseQuotient(state->inertia); // local angular velocity at time n+1/2
	if (densityScaling) angVel_b_half*=state->densityScaling;
	const Quaternionr dotQ_half=DotQ(angVel_b_half,Q_half); // dQ/dt at time n+1/2
	state->ori=state->ori+dt*dotQ_half; // Q at time n+1
	state->angVel=state->ori*angVel_b_half; // global angular velocity at time n+1/2

	if(scene->forces.getMoveRotUsed() && scene->forces.getRot(id)!=Vector3r::Zero()) {
		Vector3r r(scene->forces.getRot(id));
		Real norm=r.norm(); r/=norm;
		Quaternionr q(AngleAxisr(norm,r));
		state->ori=q*state->ori;
	}
	state->ori.normalize();
}

void NewtonIntegrator::leapfrogAsphericalRotate(State* state, const Body::id_t& id, const Real& dt, const Vector3r& M){
	Matrix3r A=state->ori.conjugate().toRotationMatrix(); // rotation matrix from global to local r.f.
	leapfrogAsphericalRotate(state,A,id,dt,M);
	/*
	const Vector3r l_n = state->angMom + dt/2. * M; // global angular momentum at time n
	const Vector3r l_b_n = A*l_n; // local angular momentum at time n
	Vector3r angVel_b_n = l_b_n.cwiseQuotient(state->inertia); // local angular velocity at time n
	if (densityScaling) angVel_b_n*=state->densityScaling;
	const Quaternionr dotQ_n=DotQ(angVel_b_n,state->ori); // dQ/dt at time n
	const Quaternionr Q_half = state->ori + dt/2. * dotQ_n; // Q at time n+1/2
	state->angMom+=dt*M; // global angular momentum at time n+1/2
	const Vector3r l_b_half = A*state->angMom; // local angular momentum at time n+1/2
	Vector3r angVel_b_half = l_b_half.cwiseQuotient(state->inertia); // local angular velocity at time n+1/2
	if (densityScaling) angVel_b_half*=state->densityScaling;
	const Quaternionr dotQ_half=DotQ(angVel_b_half,Q_half); // dQ/dt at time n+1/2
	state->ori=state->ori+dt*dotQ_half; // Q at time n+1
	state->angVel=state->ori*angVel_b_half; // global angular velocity at time n+1/2

	if(scene->forces.getMoveRotUsed() && scene->forces.getRot(id)!=Vector3r::Zero()) {
		Vector3r r(scene->forces.getRot(id));
		Real norm=r.norm(); r/=norm;
		Quaternionr q(AngleAxisr(norm,r));
		state->ori=q*state->ori;
	}
	state->ori.normalize();
	*/
}


void NewtonIntegrator::leapfrogSuperquadricsRotate(Superquadrics* shape,State* state, const Body::id_t& id, const Real& dt, const Vector3r& M){

  Matrix3r A = shape->rot_mat2local;
	leapfrogAsphericalRotate(state,A,id,dt,M);
	/*
	const Vector3r l_n = state->angMom + dt/2. * M; // global angular momentum at time n
	const Vector3r l_b_n = A*l_n; // local angular momentum at time n
	Vector3r angVel_b_n = l_b_n.cwiseQuotient(state->inertia); // local angular velocity at time n

	//bool is_empty = angVel_b_n.isZero(0);
	//if (!is_empty){//rotation, this speeds up notiblly when packing

  //cout<<"no rotation"<<is_empty<<endl;
  if (densityScaling) angVel_b_n*=state->densityScaling;
  const Quaternionr dotQ_n=DotQ(angVel_b_n,state->ori); // dQ/dt at time n
  const Quaternionr Q_half = state->ori + dt/2. * dotQ_n; // Q at time n+1/2
  state->angMom+=dt*M; // global angular momentum at time n+1/2
  const Vector3r l_b_half = A*state->angMom; // local angular momentum at time n+1/2
  Vector3r angVel_b_half = l_b_half.cwiseQuotient(state->inertia); // local angular velocity at time n+1/2

  if (densityScaling) angVel_b_half*=state->densityScaling;
  const Quaternionr dotQ_half=DotQ(angVel_b_half,Q_half); // dQ/dt at time n+1/2
  state->ori=state->ori+dt*dotQ_half; // Q at time n+1
  state->angVel=state->ori*angVel_b_half; // global angular velocity at time n+1/2

  if(scene->forces.getMoveRotUsed() && scene->forces.getRot(id)!=Vector3r::Zero()) {
    Vector3r r(scene->forces.getRot(id));
    Real norm=r.norm(); r/=norm;
    Quaternionr q(AngleAxisr(norm,r));
    state->ori=q*state->ori;
  }
  state->ori.normalize();
  //
  //shape->setOrientation(state->ori);
	*/
  shape->rot_mat2local = state->ori.conjugate().toRotationMatrix();//to particle's system
  shape->rot_mat2global = state->ori.toRotationMatrix(); //to global system

}
void NewtonIntegrator::leapfrogPolySuperellipsoidRotate(PolySuperellipsoid* shape,State* state, const Body::id_t& id, const Real& dt, const Vector3r& M){

  Matrix3r A = shape->rot_mat2local;
	leapfrogAsphericalRotate(state,A,id,dt,M);
  shape->rot_mat2local = state->ori.conjugate().toRotationMatrix();//to particle's system
  shape->rot_mat2global = state->ori.toRotationMatrix(); //to global system

}

void NewtonIntegrator::leapfrogGJKParticleRotate(GJKParticle* shape,State* state, const Body::id_t& id, const Real& dt, const Vector3r& M){

  Matrix3r A = shape->rot_mat2local;
	leapfrogAsphericalRotate(state,A,id,dt,M);
  shape->rot_mat2local = state->ori.conjugate().toRotationMatrix();//to particle's system
  shape->rot_mat2global = state->ori.toRotationMatrix(); //to global system

}

bool NewtonIntegrator::get_densityScaling() {
	FOREACH(const shared_ptr<Engine> e, Omega::instance().getScene()->engines) {
		GlobalStiffnessTimeStepper* ts=dynamic_cast<GlobalStiffnessTimeStepper*>(e.get());
		if (ts && densityScaling != ts->densityScaling) LOG_WARN("density scaling is not active in the timeStepper, it will have no effect unless a scaling is specified manually for some bodies");}
	LOG_WARN("GlobalStiffnessTimeStepper not present in O.engines, density scaling will have no effect unless a scaling is specified manually for some bodies");
	return densityScaling;;
}

void NewtonIntegrator::set_densityScaling(bool dsc) {
	FOREACH(const shared_ptr<Engine> e, Omega::instance().getScene()->engines) {
		GlobalStiffnessTimeStepper* ts=dynamic_cast<GlobalStiffnessTimeStepper*>(e.get());
		if (ts) {
			ts->densityScaling=dsc;
			densityScaling=dsc;
			LOG_WARN("GlobalStiffnessTimeStepper found in O.engines and adjusted to match this setting. Revert in the the timestepper if you don't want the scaling adjusted automatically.");
			return;
		}
	} LOG_WARN("GlobalStiffnessTimeStepper not found in O.engines. Density scaling will have no effect unless a scaling is specified manually for some bodies");
}


// http://www.euclideanspace.com/physics/kinematics/angularvelocity/QuaternionDifferentiation2.pdf
Quaternionr NewtonIntegrator::DotQ(const Vector3r& angVel, const Quaternionr& Q){
	Quaternionr dotQ;
	dotQ.w() = (-Q.x()*angVel[0]-Q.y()*angVel[1]-Q.z()*angVel[2])/2;
	dotQ.x() = ( Q.w()*angVel[0]-Q.z()*angVel[1]+Q.y()*angVel[2])/2;
	dotQ.y() = ( Q.z()*angVel[0]+Q.w()*angVel[1]-Q.x()*angVel[2])/2;
	dotQ.z() = (-Q.y()*angVel[0]+Q.x()*angVel[1]+Q.w()*angVel[2])/2;
	return dotQ;
}
