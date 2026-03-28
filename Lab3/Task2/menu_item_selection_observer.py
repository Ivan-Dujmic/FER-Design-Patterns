from commands.command import Command
from menu_item import MenuItem
from selection_observer import SelectionObserver

class MenuItemSelectionObserver(MenuItem, SelectionObserver):
    def __init__(self, command: Command, menu, label: str):
        MenuItem.__init__(self, command)
        self.menu = menu
        self.label: str = label

    def update_selection(self, size):
        self.menu.entryconfig(self.label, state='normal' if size > 0 else 'disabled')