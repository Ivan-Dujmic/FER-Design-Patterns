from abc import ABC, abstractmethod

class UndoManagerObserver(ABC):
    @abstractmethod
    def undo_stack_changed(self, size: int):
        pass

    @abstractmethod
    def redo_stack_changed(self, size: int):
        pass