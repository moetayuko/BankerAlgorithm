# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/dianlujitao/PycharmProjects/BankerAlgorithm/Ui/Ui_ReleaseDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ReleaseDialog(object):
    def setupUi(self, ReleaseDialog):
        ReleaseDialog.setObjectName("ReleaseDialog")
        ReleaseDialog.resize(267, 138)
        ReleaseDialog.setMinimumSize(QtCore.QSize(267, 138))
        ReleaseDialog.setMaximumSize(QtCore.QSize(267, 138))
        self.buttonBox = QtWidgets.QDialogButtonBox(ReleaseDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 80, 231, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(ReleaseDialog)
        self.widget.setGeometry(QtCore.QRect(30, 20, 211, 35))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.spinBox = QtWidgets.QSpinBox(self.widget)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)

        self.retranslateUi(ReleaseDialog)
        self.buttonBox.accepted.connect(ReleaseDialog.accept)
        self.buttonBox.rejected.connect(ReleaseDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ReleaseDialog)

    def retranslateUi(self, ReleaseDialog):
        _translate = QtCore.QCoreApplication.translate
        ReleaseDialog.setWindowTitle(_translate("ReleaseDialog", "释放资源"))
        self.label.setText(_translate("ReleaseDialog", "进程编号"))

