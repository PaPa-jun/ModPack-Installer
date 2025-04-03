from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class ImportPage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.pageLayout = QVBoxLayout()
        self.setLayout(self.pageLayout)

        label = QLabel("导入")
        self.pageLayout.addWidget(label)