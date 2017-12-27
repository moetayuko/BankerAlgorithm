from PyQt5.QtWidgets import QMainWindow
from InitWizard import InitWizard
from ReleaseDialog import ReleaseDialog
from RequestDialog import RequestDialog
from Ui.Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # 初始化，生成可利用资源向量和最大需求矩阵
        self.initButton.clicked.connect(lambda x: InitWizard(self).exec())
        # 申请资源，产生资源请求向量，使用银行家算法和安全性算法检查并分配资源
        self.requestButton.clicked.connect(lambda x: RequestDialog(self).exec())
        # 释放资源
        self.releaseButton.clicked.connect(lambda x: ReleaseDialog(self).exec())
