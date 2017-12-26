from PyQt5.QtWidgets import QMainWindow
from InitWizard import InitWizard
from Ui.Ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # 初始化，生成可利用资源向量和最大需求矩阵
        self.initButton.clicked.connect(lambda x: InitWizard(self).exec())
