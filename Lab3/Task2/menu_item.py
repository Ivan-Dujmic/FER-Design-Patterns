from __future__ import annotations
from typing import TYPE_CHECKING
from commands.command import Command

if TYPE_CHECKING:
    from text_editor import TextEditor

class MenuItem():
    def __init__(self, command: Command = None, editor: TextEditor = None):
        self.command: Command = command
        self.editor: TextEditor = editor

    def set_command(self, command: Command):
        self.command = command

    def clicked(self):
        if self.command:
            self.command.execute(self.editor)