from PyQt5 import QtCore

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow

from GlobalMap import GlobalMap
from InitWizard import InitWizard
from MaxDialog import MaxDialog
from ReleaseDialog import ReleaseDialog
from RequestDialog import RequestDialog
from Ui.Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # 初始化，生成可利用资源向量和最大需求矩阵
        self.initButton.clicked.connect(self.show_init_wizard)
        # 显示最大需求矩阵
        self.maxButton.clicked.connect(lambda x: MaxDialog(self).show())
        # 申请资源，产生资源请求向量，使用银行家算法和安全性算法检查并分配资源
        self.requestButton.clicked.connect(self.show_request_dialog)
        # 释放资源
        self.releaseButton.clicked.connect(self.show_release_dialog)

    def show_init_wizard(self):
        wizard = InitWizard(self)
        wizard.accepted.connect(self.update_available_resource)
        wizard.exec()

    def show_request_dialog(self):
        dialog = RequestDialog(self)
        dialog.accepted.connect(self.update_available_resource)
        dialog.exec()

    def show_release_dialog(self):
        dialog = ReleaseDialog(self)
        dialog.accepted.connect(self.update_available_resource)
        dialog.exec()

    def update_available_resource(self):
        num_process = int(GlobalMap.get('num_process'))
        num_resource = int(GlobalMap.get('num_resource'))

        # 可用资源表
        available = GlobalMap.get('available')
        if available is None:
            return

        model = QStandardItemModel()
        model.setColumnCount(2)
        model.setHeaderData(0, QtCore.Qt.Horizontal, "资源种类")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "资源数量")

        for i in range(num_resource):
            model.setItem(i, 0, QStandardItem(str(i)))
            model.setItem(i, 1, QStandardItem(str(available[i][0])))

        self.availableResTableView.setModel(model)

        # 已分配资源表
        allocation = GlobalMap.get('allocation')
        if allocation is None:
            return

        model = QStandardItemModel()
        model.setColumnCount(num_resource)

        for i in range(num_resource):
            model.setHeaderData(i, QtCore.Qt.Horizontal, str(i))

        for i in range(num_process):
            for j in range(num_resource):
                model.setItem(i, j, QStandardItem(str(allocation[i][j])))
            model.setHeaderData(i, QtCore.Qt.Vertical, str(i))

        self.allocationTableView.setModel(model)
