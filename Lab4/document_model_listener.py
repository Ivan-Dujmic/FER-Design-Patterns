from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from graphical_object import GraphicalObject
    from graphical_object_listener import GraphicalObjectListener

class DocumentModelListener(ABC):
    @abstractmethod
    def document_change(self):
        pass