# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapgen.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(777, 694)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.creationBar = QtWidgets.QProgressBar(self.centralwidget)
        self.creationBar.setProperty("value", 0)
        self.creationBar.setInvertedAppearance(False)
        self.creationBar.setObjectName("creationBar")
        self.gridLayout_5.addWidget(self.creationBar, 2, 0, 1, 3)
        self.tabAlgorithm = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabAlgorithm.sizePolicy().hasHeightForWidth())
        self.tabAlgorithm.setSizePolicy(sizePolicy)
        self.tabAlgorithm.setObjectName("tabAlgorithm")
        self.tabSimplex = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabSimplex.sizePolicy().hasHeightForWidth())
        self.tabSimplex.setSizePolicy(sizePolicy)
        self.tabSimplex.setStatusTip("")
        self.tabSimplex.setObjectName("tabSimplex")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabSimplex)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapAllRows)
        self.formLayout.setObjectName("formLayout")
        self.heightLabel = QtWidgets.QLabel(self.tabSimplex)
        self.heightLabel.setObjectName("heightLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.heightLabel)
        self.inputHeight = QtWidgets.QSpinBox(self.tabSimplex)
        self.inputHeight.setMinimum(1)
        self.inputHeight.setMaximum(1500)
        self.inputHeight.setSingleStep(100)
        self.inputHeight.setProperty("value", 200)
        self.inputHeight.setObjectName("inputHeight")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.inputHeight)
        self.lengthLabel = QtWidgets.QLabel(self.tabSimplex)
        self.lengthLabel.setObjectName("lengthLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lengthLabel)
        self.inputLength = QtWidgets.QSpinBox(self.tabSimplex)
        self.inputLength.setMinimum(1)
        self.inputLength.setMaximum(1500)
        self.inputLength.setSingleStep(100)
        self.inputLength.setProperty("value", 200)
        self.inputLength.setObjectName("inputLength")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.inputLength)
        spacerItem = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.pushEverythingUpLabel = QtWidgets.QLabel(self.tabSimplex)
        self.pushEverythingUpLabel.setObjectName("pushEverythingUpLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.pushEverythingUpLabel)
        self.inputCalcA = QtWidgets.QDoubleSpinBox(self.tabSimplex)
        self.inputCalcA.setSingleStep(0.02)
        self.inputCalcA.setProperty("value", 0.05)
        self.inputCalcA.setObjectName("inputCalcA")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.inputCalcA)
        self.pushEdgesDownLabel = QtWidgets.QLabel(self.tabSimplex)
        self.pushEdgesDownLabel.setObjectName("pushEdgesDownLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.pushEdgesDownLabel)
        self.inputCalcB = QtWidgets.QDoubleSpinBox(self.tabSimplex)
        self.inputCalcB.setSingleStep(0.1)
        self.inputCalcB.setProperty("value", 1.0)
        self.inputCalcB.setObjectName("inputCalcB")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.inputCalcB)
        self.progressOfDropdownLabel = QtWidgets.QLabel(self.tabSimplex)
        self.progressOfDropdownLabel.setObjectName("progressOfDropdownLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.progressOfDropdownLabel)
        self.inputCalcC = QtWidgets.QDoubleSpinBox(self.tabSimplex)
        self.inputCalcC.setSingleStep(0.1)
        self.inputCalcC.setProperty("value", 1.5)
        self.inputCalcC.setObjectName("inputCalcC")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.inputCalcC)
        spacerItem1 = QtWidgets.QSpacerItem(20, 300, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(12, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.generateButton = QtWidgets.QPushButton(self.tabSimplex)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generateButton.sizePolicy().hasHeightForWidth())
        self.generateButton.setSizePolicy(sizePolicy)
        self.generateButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.generateButton.setCheckable(False)
        self.generateButton.setObjectName("generateButton")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.generateButton)
        self.gradualUpdateSLOWLabel = QtWidgets.QLabel(self.tabSimplex)
        self.gradualUpdateSLOWLabel.setObjectName("gradualUpdateSLOWLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.gradualUpdateSLOWLabel)
        self.inputGradual = QtWidgets.QCheckBox(self.tabSimplex)
        self.inputGradual.setObjectName("inputGradual")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.inputGradual)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.tabAlgorithm.addTab(self.tabSimplex, "")
        self.tabVoronoi = QtWidgets.QWidget()
        self.tabVoronoi.setEnabled(True)
        self.tabVoronoi.setObjectName("tabVoronoi")
        self.tabAlgorithm.addTab(self.tabVoronoi, "")
        self.gridLayout_5.addWidget(self.tabAlgorithm, 0, 1, 1, 1)
        self.MainImage = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainImage.sizePolicy().hasHeightForWidth())
        self.MainImage.setSizePolicy(sizePolicy)
        self.MainImage.setMouseTracking(False)
        self.MainImage.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.MainImage.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        self.MainImage.setObjectName("MainImage")
        self.gridLayout_5.addWidget(self.MainImage, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabAlgorithm.setCurrentIndex(0)
        self.generateButton.clicked.connect(MainWindow.generateButton)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.heightLabel.setText(_translate("MainWindow", "Pixel height"))
        self.lengthLabel.setText(_translate("MainWindow", "Pixel length"))
        self.pushEverythingUpLabel.setText(_translate("MainWindow", "Push everything up"))
        self.pushEdgesDownLabel.setText(_translate("MainWindow", "Push edges down"))
        self.progressOfDropdownLabel.setText(_translate("MainWindow", "Progress of dropdown"))
        self.generateButton.setText(_translate("MainWindow", "Generate Simplex"))
        self.gradualUpdateSLOWLabel.setText(_translate("MainWindow", "Gradual update (SLOW)"))
        self.tabAlgorithm.setTabText(self.tabAlgorithm.indexOf(self.tabSimplex), _translate("MainWindow", "Simplex"))
        self.tabAlgorithm.setTabText(self.tabAlgorithm.indexOf(self.tabVoronoi), _translate("MainWindow", "Voronoi"))

