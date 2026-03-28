from commands.command import Command
from menu_item import MenuItem
from undo_manager_observer import UndoManagerObserver

class MenuItemRedoObserver(MenuItem, UndoManagerObserver):
    def __init__(self, command: Command, menu, label: str):
        MenuItem.__init__(self, command)
        self.menu = menu
        self.label: str = label

    def undo_stack_changed(self, size):
        pass

    def redo_stack_changed(self, size):
        self.menu.entryconfig(self.label, state='normal' if size > 0 else 'disabled')