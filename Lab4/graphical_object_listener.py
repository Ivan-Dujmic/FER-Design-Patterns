from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from graphical_object import GraphicalObject

class GraphicalObjectListener(ABC):
    @abstractmethod
    def graphical_object_changed(self, graphical_object: GraphicalObject):
        pass
        
    @abstractmethod
    def graphical_object_selection_changed(self, graphical_object: GraphicalObject):
        pass