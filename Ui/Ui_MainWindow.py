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
        self.initButton = QtWidgets.QPushButton(self.centralwidget)
        self.initButton.setGeometry(QtCore.QRect(100, 410, 110, 39))
        self.initButton.setObjectName("initButton")
        self.requestButton = QtWidgets.QPushButton(self.centralwidget)
        self.requestButton.setGeometry(QtCore.QRect(280, 400, 110, 39))
        self.requestButton.setObjectName("requestButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "银行家算法"))
        self.initButton.setText(_translate("MainWindow", "初始化"))
        self.requestButton.setText(_translate("MainWindow", "申请资源"))

