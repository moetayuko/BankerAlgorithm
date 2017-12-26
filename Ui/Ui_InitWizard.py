# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dianlujitao/PycharmProjects/BankerAlgorithm/Ui/Ui_InitWizard.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InitWizard(object):
    def setupUi(self, InitWizard):
        InitWizard.setObjectName("InitWizard")
        InitWizard.resize(725, 530)
        self.wizardPage1 = QtWidgets.QWizardPage()
        self.wizardPage1.setObjectName("wizardPage1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.wizardPage1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.processCountSpinBox = QtWidgets.QSpinBox(self.wizardPage1)
        self.processCountSpinBox.setObjectName("processCountSpinBox")
        self.gridLayout.addWidget(self.processCountSpinBox, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.wizardPage1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.wizardPage1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.resourceCountSpinBox = QtWidgets.QSpinBox(self.wizardPage1)
        self.resourceCountSpinBox.setObjectName("resourceCountSpinBox")
        self.gridLayout.addWidget(self.resourceCountSpinBox, 2, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 2, 1, 1, 1)
        InitWizard.addPage(self.wizardPage1)
        self.wizardPage2 = QtWidgets.QWizardPage()
        self.wizardPage2.setObjectName("wizardPage2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.wizardPage2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.availableTableView = QtWidgets.QTableView(self.wizardPage2)
        self.availableTableView.setObjectName("availableTableView")
        self.verticalLayout.addWidget(self.availableTableView)
        InitWizard.addPage(self.wizardPage2)
        self.wizardPage3 = QtWidgets.QWizardPage()
        self.wizardPage3.setObjectName("wizardPage3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.wizardPage3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.maxTableView = QtWidgets.QTableView(self.wizardPage3)
        self.maxTableView.setObjectName("maxTableView")
        self.verticalLayout_2.addWidget(self.maxTableView)
        InitWizard.addPage(self.wizardPage3)

        self.retranslateUi(InitWizard)
        QtCore.QMetaObject.connectSlotsByName(InitWizard)

    def retranslateUi(self, InitWizard):
        _translate = QtCore.QCoreApplication.translate
        InitWizard.setWindowTitle(_translate("InitWizard", "初始化向导"))
        self.label_2.setText(_translate("InitWizard", "资源个数"))
        self.label.setText(_translate("InitWizard", "进程个数"))
        self.wizardPage2.setTitle(_translate("InitWizard", "可利用资源"))
        self.wizardPage3.setTitle(_translate("InitWizard", "最大需求"))

