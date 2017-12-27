import numpy as np
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QMetaObject
from PyQt5.QtWidgets import QDialog, QMessageBox

from GlobalMap import GlobalMap
from Ui.Ui_ReleaseDialog import Ui_ReleaseDialog


class ReleaseDialog(QDialog, Ui_ReleaseDialog):
    def __init__(self, parent=None):
        super(ReleaseDialog, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.allocation = GlobalMap.get('allocation')

    def showEvent(self, a0: QtGui.QShowEvent):
        # 分配矩阵不存在，退出
        if self.allocation is None:
            QMessageBox.warning(self, '错误', '请先分配资源！')
            QMetaObject.invokeMethod(self, 'close', QtCore.Qt.QueuedConnection)
            return

        self.spinBox.setMaximum(GlobalMap.get('num_process') - 1)

    def accept(self):
        process = int(self.spinBox.text())
        if not self.allocation[process].any():
            QMessageBox.warning(self, '错误', '选定进程没有分配资源')
            return

        available = GlobalMap.get('available')
        available += self.allocation[process, np.newaxis].T
        self.allocation[process, :] = 0

        GlobalMap.set('available', available)
        GlobalMap.set('allocation', self.allocation)
        QMessageBox.warning(self, '提示', '释放成功')
        QDialog.accept(self)
