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

        # File menu with quit action
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)
        # Edit menu with additional actions
        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        window_menu = menu_bar.addMenu("Window")
        settings_menu = menu_bar.addMenu("Settings")
        help_menu = menu_bar.addMenu("Help")

    def quit_app(self):
        self.app.quit()
