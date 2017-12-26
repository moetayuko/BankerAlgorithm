from PyQt5 import QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWizard

from SpinBoxDelegate import SpinBoxDelegate
from Ui.Ui_InitWizard import Ui_InitWizard
from GlobalMap import *

import numpy as np


class InitWizard(QWizard, Ui_InitWizard):
    def __init__(self, parent=None):
        super(InitWizard, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.wizardPage1.validatePage = self.save_num

        self.wizardPage2.initializePage = self.init_available_resource_page
        self.wizardPage2.validatePage = self.save_available_resource

        self.wizardPage3.initializePage = self.init_max_resource_page
        self.wizardPage3.validatePage = self.save_max_resource

        # 清除分配矩阵
        GlobalMap.del_map('allocation')

    def save_num(self):
        # 进程数量
        GlobalMap.set('num_process', int(self.processCountSpinBox.text()))
        # 资源种类
        GlobalMap.set('num_resource', int(self.resourceCountSpinBox.text()))
        return True

    def init_available_resource_page(self):
        num_resource = int(GlobalMap.get('num_resource'))

        model = QStandardItemModel()
        model.setColumnCount(2)
        model.setHeaderData(0, QtCore.Qt.Horizontal, "资源种类")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "资源数量")
        for i in range(num_resource):
            idx = QStandardItem(str(i))
            idx.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            model.setItem(i, 0, idx)
            model.setItem(i, 1, QStandardItem("0"))

        self.availableTableView.setItemDelegateForColumn(1, SpinBoxDelegate())
        self.availableTableView.setModel(model)

    def save_available_resource(self):
        model = self.availableTableView.model()
        size = model.rowCount()
        available = np.zeros(size)

        for i in range(size):
            available[i] = int(model.item(i, 1).text())

        # 可利用资源向量
        GlobalMap.set('available', available)

        return True

    def init_max_resource_page(self):
        num_process = int(GlobalMap.get('num_process'))
        num_resource = int(GlobalMap.get('num_resource'))

        model = QStandardItemModel()
        model.setColumnCount(num_resource)

        for i in range(num_resource):
            model.setHeaderData(i, QtCore.Qt.Horizontal, str(i))

        for i in range(num_process):
            for j in range(num_resource):
                model.setItem(i, j, QStandardItem("0"))
            model.setHeaderData(i, QtCore.Qt.Vertical, str(i))

        self.maxTableView.setItemDelegate(SpinBoxDelegate())
        self.maxTableView.setModel(model)

    def save_max_resource(self):
        model = self.maxTableView.model()
        num_process = model.rowCount()
        num_resource = model.columnCount()
        max_need = np.zeros((num_process, num_resource))

        for i in range(num_process):
            for j in range(num_resource):
                max_need[i][j] = int(model.item(i, j).text())

        # 最大需求矩阵，max_need[i][j]表示进程i对j类资源的最大需求
        GlobalMap.set('max_need', max_need)

        return True
