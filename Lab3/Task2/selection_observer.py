from abc import ABC, abstractmethod

class SelectionObserver(ABC):
    @abstractmethod
    def update_selection(self, has_selection: bool):
        pass