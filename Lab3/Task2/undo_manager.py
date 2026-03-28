from collections import deque
from edit_action import EditAction
from undo_manager_observer import UndoManagerObserver

class UndoManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_initialized') and self._initialized:
            return
        self._initialized = True
        
        self.undo_stack: deque[EditAction] = deque()
        self.redo_stack: deque[EditAction] = deque()
        self.observers: list[UndoManagerObserver] = []

    def undo(self):
        if self.undo_stack:
            action = self.undo_stack.pop()
            self.notify_undo_stack_changed()
            action.execute_undo()
            self.redo_stack.append(action)
            self.notify_redo_stack_changed()

    def push(self, c: EditAction):
        if self.redo_stack:
            self.redo_stack.clear()
            self.notify_redo_stack_changed()
        self.undo_stack.append(c)
        self.notify_undo_stack_changed()

    def redo(self):
        if self.redo_stack:
            action = self.redo_stack.pop()
            self.notify_redo_stack_changed()
            action.execute_do()
            self.undo_stack.append(action)
            self.notify_undo_stack_changed()

    def attach_observer(self, observer: UndoManagerObserver):
        if observer not in self.observers:
            self.observers.append(observer)
            observer.undo_stack_changed(len(self.undo_stack))
            observer.redo_stack_changed(len(self.redo_stack))

    def detach_observer(self, observer: UndoManagerObserver):
        if observer in self.observers:
            self.observers.remove(observer)
            observer.undo_stack_changed(len(self.undo_stack))
            observer.redo_stack_changed(len(self.redo_stack))

    def notify_undo_stack_changed(self):
        for observer in self.observers:
            observer.undo_stack_changed(len(self.undo_stack))

    def notify_redo_stack_changed(self):
        for observer in self.observers:
            observer.redo_stack_changed(len(self.redo_stack))