# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controller-b.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Controller(object):
    def setupUi(self, Controller):
        Controller.setObjectName(_fromUtf8("Controller"))
        Controller.resize(290, 495)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Controller.sizePolicy().hasHeightForWidth())
        Controller.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/sudodem-favicon.xpm")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Controller.setWindowIcon(icon)
        self.gridLayout_3 = QtGui.QGridLayout(Controller)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.controllerTabs = QtGui.QTabWidget(Controller)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.controllerTabs.sizePolicy().hasHeightForWidth())
        self.controllerTabs.setSizePolicy(sizePolicy)
        self.controllerTabs.setObjectName(_fromUtf8("controllerTabs"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setMargin(6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.loadButton = QtGui.QPushButton(self.tab)
        self.loadButton.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadButton.sizePolicy().hasHeightForWidth())
        self.loadButton.setSizePolicy(sizePolicy)
        self.loadButton.setMinimumSize(QtCore.QSize(0, 0))
        self.loadButton.setObjectName(_fromUtf8("loadButton"))
        self.horizontalLayout_2.addWidget(self.loadButton)
        self.saveButton = QtGui.QPushButton(self.tab)
        self.saveButton.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setMinimumSize(QtCore.QSize(0, 0))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout_2.addWidget(self.saveButton)
        self.inspectButton = QtGui.QPushButton(self.tab)
        self.inspectButton.setObjectName(_fromUtf8("inspectButton"))
        self.horizontalLayout_2.addWidget(self.inspectButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(6)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_6)
        self.realTimeLabel = QtGui.QLabel(self.tab)
        self.realTimeLabel.setObjectName(_fromUtf8("realTimeLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.realTimeLabel)
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_7)
        self.virtTimeLabel = QtGui.QLabel(self.tab)
        self.virtTimeLabel.setObjectName(_fromUtf8("virtTimeLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.virtTimeLabel)
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_8)
        self.iterLabel = QtGui.QLabel(self.tab)
        self.iterLabel.setWordWrap(True)
        self.iterLabel.setObjectName(_fromUtf8("iterLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.iterLabel)
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_9)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.dtFixedRadio = QtGui.QRadioButton(self.tab)
        self.dtFixedRadio.setChecked(True)
        self.dtFixedRadio.setObjectName(_fromUtf8("dtFixedRadio"))
        self.horizontalLayout.addWidget(self.dtFixedRadio)
        self.dtDynRadio = QtGui.QRadioButton(self.tab)
        self.dtDynRadio.setEnabled(False)
        self.dtDynRadio.setObjectName(_fromUtf8("dtDynRadio"))
        self.horizontalLayout.addWidget(self.dtDynRadio)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.dtEdit = QtGui.QLineEdit(self.tab)
        self.dtEdit.setEnabled(False)
        self.dtEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.dtEdit.setObjectName(_fromUtf8("dtEdit"))
        self.verticalLayout.addWidget(self.dtEdit)
        self.formLayout.setLayout(4, QtGui.QFormLayout.FieldRole, self.verticalLayout)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.fileLabel = QtGui.QLabel(self.tab)
        self.fileLabel.setObjectName(_fromUtf8("fileLabel"))
        self.horizontalLayout_5.addWidget(self.fileLabel)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setMargin(6)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.playButton = QtGui.QPushButton(self.tab)
        self.playButton.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playButton.sizePolicy().hasHeightForWidth())
        self.playButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.playButton.setFont(font)
        self.playButton.setIconSize(QtCore.QSize(32, 32))
        self.playButton.setDefault(True)
        self.playButton.setFlat(False)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.horizontalLayout_3.addWidget(self.playButton)
        self.pauseButton = QtGui.QPushButton(self.tab)
        self.pauseButton.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pauseButton.sizePolicy().hasHeightForWidth())
        self.pauseButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pauseButton.setFont(font)
        self.pauseButton.setIconSize(QtCore.QSize(32, 32))
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        self.horizontalLayout_3.addWidget(self.pauseButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setMargin(0)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.stepButton = QtGui.QPushButton(self.tab)
        self.stepButton.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stepButton.sizePolicy().hasHeightForWidth())
        self.stepButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stepButton.setFont(font)
        self.stepButton.setIconSize(QtCore.QSize(32, 32))
        self.stepButton.setObjectName(_fromUtf8("stepButton"))
        self.gridLayout_9.addWidget(self.stepButton, 0, 0, 1, 1)
        self.subStepCheckbox = QtGui.QCheckBox(self.tab)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.subStepCheckbox.setFont(font)
        self.subStepCheckbox.setObjectName(_fromUtf8("subStepCheckbox"))
        self.gridLayout_9.addWidget(self.subStepCheckbox, 1, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_9)
        self.reloadButton = QtGui.QPushButton(self.tab)
        self.reloadButton.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reloadButton.sizePolicy().hasHeightForWidth())
        self.reloadButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.reloadButton.setFont(font)
        self.reloadButton.setIconSize(QtCore.QSize(32, 32))
        self.reloadButton.setObjectName(_fromUtf8("reloadButton"))
        self.horizontalLayout_4.addWidget(self.reloadButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.show3dButton = QtGui.QPushButton(self.tab)
        self.show3dButton.setCheckable(True)
        self.show3dButton.setObjectName(_fromUtf8("show3dButton"))
        self.gridLayout_2.addWidget(self.show3dButton, 0, 0, 1, 1)
        self.referenceButton = QtGui.QPushButton(self.tab)
        self.referenceButton.setObjectName(_fromUtf8("referenceButton"))
        self.gridLayout_2.addWidget(self.referenceButton, 0, 1, 1, 1)
        self.centerButton = QtGui.QPushButton(self.tab)
        self.centerButton.setObjectName(_fromUtf8("centerButton"))
        self.gridLayout_2.addWidget(self.centerButton, 0, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.controllerTabs.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_7.setMargin(0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.displayCombo = QtGui.QComboBox(self.tab_2)
        self.displayCombo.setObjectName(_fromUtf8("displayCombo"))
        self.gridLayout_7.addWidget(self.displayCombo, 0, 0, 1, 1)
        self.displayArea = QtGui.QScrollArea(self.tab_2)
        self.displayArea.setWidgetResizable(True)
        self.displayArea.setObjectName(_fromUtf8("displayArea"))
        self.displayAreaWidget = QtGui.QWidget()
        self.displayAreaWidget.setGeometry(QtCore.QRect(0, 0, 284, 437))
        self.displayAreaWidget.setObjectName(_fromUtf8("displayAreaWidget"))
        self.displayArea.setWidget(self.displayAreaWidget)
        self.gridLayout_7.addWidget(self.displayArea, 1, 0, 1, 1)
        self.controllerTabs.addTab(self.tab_2, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.generatorCombo = QtGui.QComboBox(self.tab_4)
        self.generatorCombo.setObjectName(_fromUtf8("generatorCombo"))
        self.gridLayout_5.addWidget(self.generatorCombo, 0, 0, 1, 1)
        self.generatorArea = QtGui.QScrollArea(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.generatorArea.sizePolicy().hasHeightForWidth())
        self.generatorArea.setSizePolicy(sizePolicy)
        self.generatorArea.setMinimumSize(QtCore.QSize(0, 0))
        self.generatorArea.setWidgetResizable(True)
        self.generatorArea.setObjectName(_fromUtf8("generatorArea"))
        self.generatorAreaWidget = QtGui.QWidget()
        self.generatorAreaWidget.setGeometry(QtCore.QRect(0, 0, 500, 500))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generatorAreaWidget.sizePolicy().hasHeightForWidth())
        self.generatorAreaWidget.setSizePolicy(sizePolicy)
        self.generatorAreaWidget.setMinimumSize(QtCore.QSize(500, 500))
        self.generatorAreaWidget.setMaximumSize(QtCore.QSize(398, 336))
        self.generatorAreaWidget.setObjectName(_fromUtf8("generatorAreaWidget"))
        self.generatorArea.setWidget(self.generatorAreaWidget)
        self.gridLayout_5.addWidget(self.generatorArea, 1, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.generatorMemoryCheck = QtGui.QCheckBox(self.tab_4)
        self.generatorMemoryCheck.setEnabled(False)
        self.generatorMemoryCheck.setCheckable(False)
        self.generatorMemoryCheck.setChecked(False)
        self.generatorMemoryCheck.setObjectName(_fromUtf8("generatorMemoryCheck"))
        self.gridLayout_4.addWidget(self.generatorMemoryCheck, 0, 0, 1, 1)
        self.generatorFilenameEdit = QtGui.QLineEdit(self.tab_4)
        self.generatorFilenameEdit.setObjectName(_fromUtf8("generatorFilenameEdit"))
        self.gridLayout_4.addWidget(self.generatorFilenameEdit, 0, 1, 1, 2)
        self.generatorAutoCheck = QtGui.QCheckBox(self.tab_4)
        self.generatorAutoCheck.setChecked(True)
        self.generatorAutoCheck.setObjectName(_fromUtf8("generatorAutoCheck"))
        self.gridLayout_4.addWidget(self.generatorAutoCheck, 1, 0, 1, 2)
        self.generateButton = QtGui.QPushButton(self.tab_4)
        self.generateButton.setObjectName(_fromUtf8("generateButton"))
        self.gridLayout_4.addWidget(self.generateButton, 1, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 2, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.controllerTabs.addTab(self.tab_4, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_8 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_8.setMargin(0)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.pythonCombo = QtGui.QComboBox(self.tab_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        self.pythonCombo.setFont(font)
        self.pythonCombo.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.pythonCombo.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pythonCombo.setAutoFillBackground(False)
        self.pythonCombo.setEditable(True)
        self.pythonCombo.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        self.pythonCombo.setMinimumContentsLength(1)
        self.pythonCombo.setDuplicatesEnabled(False)
        self.pythonCombo.setObjectName(_fromUtf8("pythonCombo"))
        self.verticalLayout_4.addWidget(self.pythonCombo)
        self.label = QtGui.QLabel(self.tab_3)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_4.addWidget(self.label)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.gridLayout_8.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.controllerTabs.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.controllerTabs, 0, 0, 1, 1)

        self.retranslateUi(Controller)
        self.controllerTabs.setCurrentIndex(0)
        QtCore.QObject.connect(self.loadButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Controller.loadSlot)
        QtCore.QObject.connect(self.saveButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Controller.saveSlot)
        QtCore.QObject.connect(self.dtFixedRadio, QtCore.SIGNAL(_fromUtf8("clicked()")), Controller.dtFixedSlot)
        QtCore.QObject.connect(self.dtDynRadio, QtCore.SIGNAL(_fromUtf8("clicked()")), Controller.dtDynSlot)
        QtCore.QObject.connect(self.dtEdit, QtCore.SIGNAL(_fromUtf8("editingFinished()")), Controller.dtEditedSlot)
        QtCore.QObject.connect(self.playButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Controller.playSlot)
        QtCore.QObject.connect(self.pauseButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Controller.pauseSlot)
        QtCore.QObject.connect(self.referenceButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Controller.setReferenceSlot)
        QtCore.QObject.connect(self.centerButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Controller.centerSlot)
        QtCore.QObject.connect(self.generateButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Controller.generateSlot)
        QtCore.QObject.connect(self.dtEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), Controller.dtEditNoupdateSlot)
        QtCore.QObject.connect(self.dtEdit, QtCore.SIGNAL(_fromUtf8("cursorPositionChanged(int,int)")), Controller.dtEditNoupdateSlot)
        QtCore.QObject.connect(self.generatorCombo, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), Controller.generatorComboSlot)
        QtCore.QObject.connect(self.displayCombo, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), Controller.displayComboSlot)
        QtCore.QObject.connect(self.pythonCombo, QtCore.SIGNAL(_fromUtf8("activated(QString)")), Controller.pythonComboSlot)
        QtCore.QObject.connect(self.inspectButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Controller.inspectSlot)
        QtCore.QObject.connect(self.reloadButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Controller.reloadSlot)
        QtCore.QObject.connect(self.stepButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Controller.stepSlot)
        QtCore.QObject.connect(self.subStepCheckbox, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")), Controller.subStepSlot)
        QtCore.QObject.connect(self.show3dButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), Controller.show3dSlot)
        QtCore.QMetaObject.connectSlotsByName(Controller)

    def retranslateUi(self, Controller):
        Controller.setWindowTitle(_translate("Controller", "SudoDEM2D", None))
        self.loadButton.setText(_translate("Controller", "Load", None))
        self.saveButton.setText(_translate("Controller", "Save", None))
        self.inspectButton.setText(_translate("Controller", "Inspect", None))
        self.label_6.setText(_translate("Controller", "real", None))
        self.realTimeLabel.setText(_translate("Controller", "00:00:00", None))
        self.label_7.setText(_translate("Controller", "virt", None))
        self.virtTimeLabel.setText(_translate("Controller", "00:000.000m000μ000n", None))
        self.label_8.setText(_translate("Controller", "iter", None))
        self.iterLabel.setText(_translate("Controller", "#0, 0.0/s", None))
        self.label_9.setText(_translate("Controller", "Δt", None))
        self.dtFixedRadio.setText(_translate("Controller", "fixed", None))
        self.dtDynRadio.setText(_translate("Controller", "time stepper", None))
        self.fileLabel.setText(_translate("Controller", "[no file]", None))
        self.playButton.setText(_translate("Controller", "▶", None))
        self.pauseButton.setText(_translate("Controller", "▮▮", None))
        self.stepButton.setText(_translate("Controller", "▶▮", None))
        self.subStepCheckbox.setText(_translate("Controller", "sub-step", None))
        self.reloadButton.setText(_translate("Controller", "↻", None))
        self.show3dButton.setText(_translate("Controller", "Show", None))
        self.referenceButton.setText(_translate("Controller", "Reference", None))
        self.centerButton.setText(_translate("Controller", "Center", None))
        self.controllerTabs.setTabText(self.controllerTabs.indexOf(self.tab), _translate("Controller", "Simulation", None))
        self.controllerTabs.setTabText(self.controllerTabs.indexOf(self.tab_2), _translate("Controller", "Display", None))
        self.generatorMemoryCheck.setText(_translate("Controller", "memory slot", None))
        self.generatorFilenameEdit.setText(_translate("Controller", "/tmp/scene.sudodem.gz", None))
        self.generatorAutoCheck.setText(_translate("Controller", "open automatically", None))
        self.generateButton.setText(_translate("Controller", "Generate", None))
        self.controllerTabs.setTabText(self.controllerTabs.indexOf(self.tab_4), _translate("Controller", "Generate", None))
        self.label.setText(_translate("Controller", "<i>(Output appears in the terminal)</i>", None))
        self.controllerTabs.setTabText(self.controllerTabs.indexOf(self.tab_3), _translate("Controller", "Python", None))

import img_rc
