from abc import ABC, abstractmethod

class TextObserver(ABC):
    @abstractmethod
    def update_text(self, start_line: int, end_line: int):
        pass