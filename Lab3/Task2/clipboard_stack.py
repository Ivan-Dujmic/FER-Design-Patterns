from collections import deque
from clipboard_observer import ClipboardObserver

class ClipboardStack:
    def __init__(self):
        self.stack: deque[str] = deque()
        self.observers: list[ClipboardObserver] = []
        
    def push(self, text: str) -> bool:
        if text != "":
            self.stack.append(text)
            self.notify_observers()

    def pop(self) -> bool:
        if self.stack:
            self.stack.pop()
            self.notify_observers()
            return True
        return False
    
    def peek(self) -> str:
        if self.stack:
            return self.stack[-1]
        return ""

    def clear(self):
        if self.stack:
            self.stack.clear()
            self.notify_observers()

    def attach_observer(self, observer: ClipboardObserver):
        if observer not in self.observers:
            self.observers.append(observer)
            observer.update_clipboard(len(self.stack))

    def detach_observer(self, observer: ClipboardObserver):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update_clipboard(len(self.stack))