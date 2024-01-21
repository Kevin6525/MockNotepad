from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Kevin's Notepad")

        # Menu options/actions for our app
        menu_bar = self.menuBar()
        # This line is only required for Mac OS and not Windows
        menu_bar.setNativeMenuBar(False) 
        file_menu = menu_bar.addMenu("&File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

    def quit_app(self):
        self.app.quit()
