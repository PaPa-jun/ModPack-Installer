from PyQt6.QtWidgets import QStackedWidget

class PageStack(QStackedWidget):
    """
    Pagestack widget.
    """
    def __init__(self):
        super().__init__()

    def initUi(self):
        self