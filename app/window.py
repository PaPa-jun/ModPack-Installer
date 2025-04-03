from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout
from PyQt6.QtCore import QSize
from app.views.home import HomePage
from app.widgets.navigation import NavigationItem, NavigationBar

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
        self.centraLayout.setContentsMargins(0, 0, 0, 0)
        self.centraLayout.setSpacing(0)

        self.navBar = NavigationBar()
        self.centraLayout.addWidget(self.navBar)

        homeButton = NavigationItem("assets/icons/home.svg", "主页")
        importButton = NavigationItem("assets/icons/import.svg", "Import")
        settingsButton = NavigationItem("assets/icons/settings.svg", "Settings")

        self.navBar.navigationList.addItems([homeButton, importButton], "top")
        self.navBar.navigationList.addItem(settingsButton, "bottom")
        self.navBar.navigationList.setSelectedItem(0)