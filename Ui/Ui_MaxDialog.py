# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dianlujitao/PycharmProjects/BankerAlgorithm/Ui/Ui_MaxDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MaxDialog(object):
    def setupUi(self, MaxDialog):
        MaxDialog.setObjectName("MaxDialog")
        MaxDialog.resize(685, 570)
        self.verticalLayout = QtWidgets.QVBoxLayout(MaxDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(MaxDialog)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.buttonBox = QtWidgets.QDialogButtonBox(MaxDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(MaxDialog)
        self.buttonBox.rejected.connect(MaxDialog.reject)
        self.buttonBox.accepted.connect(MaxDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(MaxDialog)

    def retranslateUi(self, MaxDialog):
        _translate = QtCore.QCoreApplication.translate
        MaxDialog.setWindowTitle(_translate("MaxDialog", "最大需求矩阵"))

