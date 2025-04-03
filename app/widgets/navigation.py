from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, pyqtSignal, QSize
from app.stylesheets.utlis import loadQss

class NavigationItem(QWidget):
    """
    Navigation item.
    """

    clickedSignal = pyqtSignal(int)
    idCounter = 0

    def __init__(self, iconPath: str = None, text: str = None):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setFixedSize(QSize(150, 50))
        self.id = NavigationItem.idCounter
        NavigationItem.idCounter += 1

        self.iconLabel = QLabel()
        self.textLabel = QLabel()
        if iconPath:
            pixmap = QPixmap(iconPath)
            self.iconLabel.setPixmap(pixmap.scaledToWidth(24, Qt.TransformationMode.SmoothTransformation))
        if text:
            self.textLabel.setText(text)
        self.initUi()
        
    def initUi(self):
        self.mainLayout = QHBoxLayout()
        self.setLayout(self.mainLayout)
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.mainLayout.setContentsMargins(25, 0, 0, 0)
        self.mainLayout.setSpacing(30)

        self.mainLayout.addWidget(self.iconLabel)
        self.mainLayout.addWidget(self.textLabel)
        
    def setText(self, text: str):
        self.textLabel.setText(text)
    
    def setIcon(self, iconPath: str):
        pixmap = QPixmap(iconPath)
        self.iconLabel.setPixmap(pixmap.scaledToWidth(24, Qt.TransformationMode.SmoothTransformation))

    def enterEvent(self, event):
        self.setStyleSheet("NavigationItem {background-color: #e0e0e0;}")
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        return super().enterEvent(event)
    
    def leaveEvent(self, event):
        self.setStyleSheet("NavigationItem {background-color: transparent;}")
        return super().leaveEvent(event)

    def mousePressEvent(self, event):
        self.setStyleSheet("NavigationItem {background-color: #c2c1c1;}")
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.clickedSignal.emit(self.id)
        self.setStyleSheet("NavigationItem {background-color: transparent;}")
        return super().mouseReleaseEvent(event)

class NavigationList(QWidget):
    """
    Navigation list widget.
    """

    itemClickedSignal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setFixedWidth(150)
        self.items = []
        self.iniUi()

    def iniUi(self):
        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)

        topArea = QWidget()
        self.topLayout = QVBoxLayout()
        topArea.setLayout(self.topLayout)
        self.mainLayout.addWidget(topArea)

        self.mainLayout.addStretch()

        bottomArea = QWidget()
        self.bottomLayout = QVBoxLayout()
        bottomArea.setLayout(self.bottomLayout)
        self.mainLayout.addWidget(bottomArea)
        
        self.topLayout.setContentsMargins(0, 0, 0, 0)
        self.topLayout.setSpacing(0)
        self.bottomLayout.setContentsMargins(0, 0, 0, 0)
        self.bottomLayout.setSpacing(0)

    def addItem(self, item: NavigationItem, area: str):
        if area == "top":
            item.clickedSignal.connect(self.onClicked)
            self.items.append(item)
            self.topLayout.addWidget(item)
        elif area == "bottom":
            item.clickedSignal.connect(self.onClicked)
            self.items.append(item)
            self.bottomLayout.addWidget(item)
        else: raise(ValueError("Wrrong area: top or bottom."))

    def addItems(self, items: list, area: str):
        for item in items:
            self.addItem(item, area)
    
    def onClicked(self, id: int):
        self.itemClickedSignal.emit(id)

    def collapse(self):
        for item in self.items:
            item.textLabel.hide()
            item.mainLayout.setContentsMargins(15, 0, 0, 0)
        self.setFixedWidth(60)

    def expand(self):
        for item in self.items:
            item.textLabel.show()
            item.mainLayout.setContentsMargins(25, 0, 0, 0)
        self.setFixedWidth(150)

class ToggleButton(QWidget):
    """
    Toggle Button.
    """

    toggledSignal = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setFixedWidth(15)
        self.expand = True
        self.initUi()

    def initUi(self):
        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.collapsePixmap = QPixmap("assets/icons/collapse.svg")
        self.expandPixmap = QPixmap("assets/icons/expand.svg")
        self.label.setPixmap(self.collapsePixmap.scaledToWidth(24, Qt.TransformationMode.SmoothTransformation))
        self.mainLayout.addWidget(self.label)

    def enterEvent(self, event):
        self.setStyleSheet("ToggleButton {background-color: #e0e0e0;}")
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        return super().enterEvent(event)
    
    def leaveEvent(self, event):
        self.setStyleSheet("ToggleButton {background-color: transparent;}")
        return super().leaveEvent(event)

    def mousePressEvent(self, event):
        self.setStyleSheet("ToggleButton {background-color: #c2c1c1;}")
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.expand = not self.expand
        if self.expand:
            self.label.setPixmap(self.collapsePixmap.scaledToWidth(24, Qt.TransformationMode.SmoothTransformation))
        else:
            self.label.setPixmap(self.expandPixmap.scaledToWidth(24, Qt.TransformationMode.SmoothTransformation))
        self.toggledSignal.emit(self.expand)
        self.setStyleSheet("ToggleButton {background-color: transparent;}")
        return super().mouseReleaseEvent(event)

class NavigationBar(QWidget):
    """
    Navigation bar widget.
    """
    def __init__(self):
        super().__init__()
        self.iniUi()

    def iniUi(self):
        self.mainLayout = QHBoxLayout()
        self.setLayout(self.mainLayout)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.navigationList = NavigationList()
        self.mainLayout.addWidget(self.navigationList)

        self.toggelButton = ToggleButton()
        self.mainLayout.addWidget(self.toggelButton)

        self.toggelButton.toggledSignal.connect(self.toggled)

    def toggled(self, expand: bool):
        if expand:
            self.navigationList.expand()
        else:
            self.navigationList.collapse()