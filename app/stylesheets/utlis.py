from pathlib import Path

def loadQss(filePath: str):
    path = Path("app/stylesheets", filePath)
    with open(path, "r") as file:
        styleSheet = file.read()
    return styleSheet