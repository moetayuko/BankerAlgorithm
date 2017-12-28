# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dianlujitao/PycharmProjects/BankerAlgorithm/Ui/Ui_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(876, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.availableResTableView = QtWidgets.QTableView(self.centralwidget)
        self.availableResTableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.availableResTableView.setObjectName("availableResTableView")
        self.gridLayout.addWidget(self.availableResTableView, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.allocationTableView = QtWidgets.QTableView(self.centralwidget)
        self.allocationTableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.allocationTableView.setObjectName("allocationTableView")
        self.gridLayout.addWidget(self.allocationTableView, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.initButton = QtWidgets.QPushButton(self.centralwidget)
        self.initButton.setObjectName("initButton")
        self.horizontalLayout.addWidget(self.initButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.maxButton = QtWidgets.QPushButton(self.centralwidget)
        self.maxButton.setObjectName("maxButton")
        self.horizontalLayout.addWidget(self.maxButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.requestButton = QtWidgets.QPushButton(self.centralwidget)
        self.requestButton.setObjectName("requestButton")
        self.horizontalLayout.addWidget(self.requestButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.releaseButton = QtWidgets.QPushButton(self.centralwidget)
        self.releaseButton.setObjectName("releaseButton")
        self.horizontalLayout.addWidget(self.releaseButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "银行家算法"))
        self.label.setText(_translate("MainWindow", "可用资源"))
        self.label_2.setText(_translate("MainWindow", "已分配资源"))
        self.initButton.setText(_translate("MainWindow", "初始化"))
        self.maxButton.setText(_translate("MainWindow", "查看最大需求"))
        self.requestButton.setText(_translate("MainWindow", "申请资源"))
        self.releaseButton.setText(_translate("MainWindow", "释放资源"))

