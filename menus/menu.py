from PySide6.QtWidgets import QMenuBar
from menus.file_menu import createFileMenu
from menus.edit_menu import createEditMenu

def createMenu(app, menu_bar, text_edit, operating_system):
    # Menu options/actions for our app
    if (operating_system.lower() == "darwin"):
        # This line is only required for Mac OS and not Windows
        menu_bar.setNativeMenuBar(False) 

    createFileMenu(menu_bar, app)
    createEditMenu(menu_bar, text_edit)


