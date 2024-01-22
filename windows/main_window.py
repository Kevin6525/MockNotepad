from PySide6.QtWidgets import QStatusBar, QMainWindow, QTextEdit, QVBoxLayout, QWidget
from menus.menu import createMenu



class MainWindow(QMainWindow):
    def __init__(self, app, operating_system):
        super().__init__()
        self.app = app
        self.setWindowTitle("Kevin's Notepad")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        v_layout = QVBoxLayout(central_widget)

        self.text_edit = QTextEdit(self)

        # Add the text editor
        v_layout.addWidget(self.text_edit)

        # Create the menu
        menu_bar = self.menuBar()
        createMenu(app, menu_bar, self.text_edit, operating_system)

        self.setStatusBar(QStatusBar(self))
