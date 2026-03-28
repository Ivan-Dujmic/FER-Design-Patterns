from commands.command import Command
from menu_item import MenuItem
from clipboard_observer import ClipboardObserver

class MenuItemClipboardObserver(MenuItem, ClipboardObserver):
    def __init__(self, command: Command, menu, label: str):
        MenuItem.__init__(self, command)
        self.menu = menu
        self.label: str = label

    def update_clipboard(self, size):
        self.menu.entryconfig(self.label, state='normal' if size > 0 else 'disabled')