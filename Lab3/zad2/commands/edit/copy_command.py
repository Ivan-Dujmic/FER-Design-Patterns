from __future__ import annotations
from typing import TYPE_CHECKING
from commands.command import Command
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

if TYPE_CHECKING:
    from text_editor import TextEditor

class CopyCommand(Command):
    def __init__(self, editor: TextEditor):
        self.editor: TextEditor = editor

    def execute(self):
        self.editor.on_ctrl_c()