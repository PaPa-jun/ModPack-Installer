from PyQt6.QtWidgets import QWidget, QVBoxLayout

class HomePage(QWidget):
    def __init__(self):
        super().__init__()

    def initUi(self):
        self.pageLayout = QVBoxLayout()
        self.setLayout(self.pageLayout)