from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QMetaObject
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QMessageBox

from GlobalMap import GlobalMap
from Ui.Ui_MaxDialog import Ui_MaxDialog


class MaxDialog(QDialog, Ui_MaxDialog):
    def __init__(self, parent=None):
        super(MaxDialog, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    def showEvent(self, a0: QtGui.QShowEvent):
        # 尚未初始化，退出
        if not GlobalMap.get('init'):
            QMessageBox.warning(self, '错误', '请先初始化！')
            QMetaObject.invokeMethod(self, 'close', QtCore.Qt.QueuedConnection)
            return

        num_process = int(GlobalMap.get('num_process'))
        num_resource = int(GlobalMap.get('num_resource'))

        # 最大需求矩阵
        max_need = GlobalMap.get('max_need')

        model = QStandardItemModel()
        model.setColumnCount(num_resource)

        for i in range(num_resource):
            model.setHeaderData(i, QtCore.Qt.Horizontal, str(i))

        for i in range(num_process):
            for j in range(num_resource):
                # 从最大需求矩阵中读取第i个进程对第j种资源的需求，显示在表格中
                model.setItem(i, j, QStandardItem(str(max_need[i][j])))
            model.setHeaderData(i, QtCore.Qt.Vertical, str(i))

        self.tableView.setModel(model)
