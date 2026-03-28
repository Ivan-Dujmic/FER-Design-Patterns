from abc import ABC, abstractmethod
from location import Location

class CursorObserver(ABC):
    # Let the observers fetch the current cursor location by themselves
    @abstractmethod
    def update_cursor_location(self):
        pass