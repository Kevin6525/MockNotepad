# Code to create the file part of our menu
def createFileMenu(menu_bar, app):
    # File menu with quit action
    file_menu = menu_bar.addMenu("File")
    createFileQuit(file_menu, app)

def createFileQuit(file_menu, app):
    quit_action = file_menu.addAction("Quit")
    quit_action.triggered.connect(lambda: quit_app(app))

def quit_app(app):
    app.quit()