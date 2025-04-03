from PyQt6.QtWidgets import QWidget, QVBoxLayout

class NavigationBar(QWidget):
    """
    Navigation bar widget.
    """
    def __init__(self):
        super().__init__()

    def iniUi(self):
        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)