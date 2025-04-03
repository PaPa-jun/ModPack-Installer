from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout
from PyQt6.QtCore import QSize
from app.views.home import HomePage

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.resize(QSize(1280, 720))
        self.setMinimumSize(400, 225)
        self.setWindowTitle("CurseForge ModPack Installer")

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.centraLayout = QHBoxLayout()
        centralWidget.setLayout(self.centraLayout)