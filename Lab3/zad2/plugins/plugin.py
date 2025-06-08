from __future__ import annotations
from typing import TYPE_CHECKING
from abc import abstractmethod
from commands.command import Command

if TYPE_CHECKING:
    from text_editor import TextEditor

class Plugin(Command):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def execute(self, editor: TextEditor = None):
        pass