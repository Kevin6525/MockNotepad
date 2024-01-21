import sys
from PySide6.QtWidgets import QApplication
from windows.main_window import MainWindow

app = QApplication(sys.argv)

window = MainWindow(app)
window.show()

app.exec()