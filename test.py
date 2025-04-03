import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from app.widgets.navigation import NavigationItem, NavigationList
from app.stylesheets.utlis import loadQss

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(loadQss("navigation.qss"))

    window = NavigationList()
    homeButton = NavigationItem("assets/icons/home.svg", "Home")
    importButton = NavigationItem("assets/icons/import.svg", "Import")
    settingsButton = NavigationItem("assets/icons/settings.svg", "Settings")
    window.addItems([homeButton, importButton], "top")
    window.addItem(settingsButton, "bottom")
    homeButton.clickedSignal.connect(lambda x: print(x))
    importButton.clickedSignal.connect(lambda x: print(x))
    settingsButton.clickedSignal.connect(lambda x: print(x))
    window.show()
    sys.exit(app.exec())
    