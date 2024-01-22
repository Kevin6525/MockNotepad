import sys
from sys import platform
from PySide6.QtWidgets import QApplication
from windows.main_window import MainWindow

app = QApplication(sys.argv)

window = MainWindow(app, platform)
window.setMinimumSize(700, 400)
window.show()

app.exec()