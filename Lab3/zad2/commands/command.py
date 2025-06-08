from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from text_editor import TextEditor

class Command(ABC):
    @abstractmethod
    def execute(self, editor: TextEditor = None):
        pass