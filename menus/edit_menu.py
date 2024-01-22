# Code to create the edit section of our menu
def createEditMenu(menu_bar, text_edit):
    edit_menu = menu_bar.addMenu("Edit")
    createEditCopy(edit_menu, text_edit)
    createEditCut(edit_menu, text_edit)
    createEditUndo(edit_menu, text_edit)
    createEditRedo(edit_menu, text_edit)

def createEditCopy(edit_menu, text_edit):
    copy_action = edit_menu.addAction("Copy")
    copy_action.triggered.connect(text_edit.copy)

def createEditCut(edit_menu, text_edit):
    cut_action = edit_menu.addAction("Cut")
    cut_action.triggered.connect(text_edit.cut)

def createEditPaste(edit_menu, text_edit):
    paste_action = edit_menu.addAction("Paste")
    # TO DO

def createEditUndo(edit_menu, text_edit):
    undo_action = edit_menu.addAction("Undo")
    undo_action.triggered.connect(text_edit.undo)

def createEditRedo(edit_menu, text_edit):
    redo_action = edit_menu.addAction("Redo")
    redo_action.triggered.connect(text_edit.redo)
