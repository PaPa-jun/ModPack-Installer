from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.pageLayout = QVBoxLayout()
        self.setLayout(self.pageLayout)

        label = QLabel("主页")
        self.pageLayout.addWidget(label)