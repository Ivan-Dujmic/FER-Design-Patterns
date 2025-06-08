from abc import ABC, abstractmethod

class ClipboardObserver(ABC):
    @abstractmethod
    def update_clipboard(self, size: int):
        pass