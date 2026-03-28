from abc import ABC, abstractmethod

class EditAction(ABC):
    @abstractmethod
    def execute_do():
        pass

    @abstractmethod
    def execute_undo():
        pass