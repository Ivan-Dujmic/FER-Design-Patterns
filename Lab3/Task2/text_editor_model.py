from location import Location
from location_range import LocationRange
from typing import Iterator
from cursor_observer import CursorObserver
from text_observer import TextObserver
from selection_observer import SelectionObserver
from string_utils import StringUtils

class TextEditorModel:
    def __init__(self, text: str = ""):
        self.lines: list[str] = text.splitlines()
        if len(self.lines) == 0:
            self.lines.append("")
        self.selection_range: LocationRange | None = None
        self.cursor_location: Location = Location(0, 0)
        self.cursor_observers: list[CursorObserver] = []
        self.text_observers: list[TextObserver] = []
        self.selection_observers: list[SelectionObserver] = []

    def get_lines(self) -> list[str]:
        return self.lines
    
    def lines_iter(self) -> Iterator[str]:
        for line in self.lines:
            yield line

    def lines_range_iter(self, begin, end) -> Iterator[str]:
        for i in range(begin, end):
            yield self.lines[i]

    # Returns the text and the range of the deletion (for command history)
    def clear(self) -> tuple[str, LocationRange]:
        range = LocationRange(Location(0, 0), Location(len(self.lines) - 1, len(self.lines[-1])))
        return self.delete_range(range)

    def get_selection_range(self) -> LocationRange | None:
        return self.selection_range
    
    def set_selection_range(self, selection_range: LocationRange | None):
        if self.selection_range != selection_range:
            self.selection_range = selection_range
            self.notify_selection_observers()

    def select_all(self):
        start = Location(0, 0)
        end = Location(len(self.lines) - 1, len(self.lines[-1]))
        self.cursor_location = end.copy()
        self.set_selection_range(LocationRange(start, end))

    def get_cursor_location(self) -> Location:
        return self.cursor_location.copy()
    
    # Mainly necessary for command history to restore cursor position
    def set_cursor_location(self, location: Location):
        if self.cursor_location != location:
            self.cursor_location = location.copy()
            self.notify_cursor_observers()
    
    def move_cursor_to_start(self):
        self.set_cursor_location(Location(0, 0))
        self.set_selection_range(None)

    def move_cursor_to_end(self):
        last_line_index = len(self.lines) - 1
        last_column_index = len(self.lines[last_line_index])
        self.set_cursor_location(Location(last_line_index, last_column_index))

    def attach_cursor_observer(self, observer: CursorObserver):
        if observer not in self.cursor_observers:
            self.cursor_observers.append(observer)
            self.notify_cursor_observers()

    def detach_cursor_observer(self, observer: CursorObserver):
        if observer in self.cursor_observers:
            self.cursor_observers.remove(observer)

    def notify_cursor_observers(self):
        for observer in self.cursor_observers:
            observer.update_cursor_location()

    def attach_text_observer(self, observer: TextObserver):
        if observer not in self.text_observers:
            self.text_observers.append(observer)
            self.notify_text_observers()

    def detach_text_observer(self, observer: TextObserver):
        if observer in self.text_observers:
            self.text_observers.remove(observer)

    def notify_text_observers(self, start: int = 0, end: int = -1):
        for observer in self.text_observers:
            observer.update_text(start, end)

    def attach_selection_observer(self, observer: SelectionObserver):
        if observer not in self.selection_observers:
            self.selection_observers.append(observer)
            self.notify_selection_observers()

    def detach_selection_observer(self, observer: SelectionObserver):
        if observer in self.selection_observers:
            self.selection_observers.remove(observer)

    def notify_selection_observers(self):
        for observer in self.selection_observers:
            observer.update_selection(self.selection_range is not None)

    def move_cursor_left(self, shift: bool = False, ctrl: bool = False):
        previous = self.cursor_location.copy()
        if self.cursor_location.get_column() > 0:
            if ctrl:
                boundary = StringUtils.find_word_boundary_left(self.lines[self.cursor_location.get_line()], self.cursor_location.get_column())
                self.cursor_location.set_column(boundary)
                if shift:
                    if not self.selection_range:
                        self.set_selection_range(LocationRange(previous, self.cursor_location.copy()))
                    else:
                        self.set_selection_range(LocationRange(self.selection_range.get_start(), self.cursor_location.copy()))
            else:
                self.cursor_location.set_column(self.cursor_location.get_column() - 1)
                if shift:
                    if not self.selection_range:
                        self.set_selection_range(LocationRange(previous, self.cursor_location.copy()))
                    else:
                        self.set_selection_range(LocationRange(self.selection_range.get_start(), self.cursor_location.copy()))
        elif self.cursor_location.get_line() > 0:
            if ctrl:
                boundary = StringUtils.find_word_boundary_left(self.lines[self.cursor_location.get_line() - 1], len(self.lines[self.cursor_location.get_line() - 1]))
                self.cursor_location.set_line(self.cursor_location.get_line() - 1)
                self.cursor_location.set_column(boundary)
                if shift:
                    if not self.selection_range:
                        self.set_selection_range(LocationRange(previous, self.cursor_location.copy()))
                    else:
                        self.set_selection_range(LocationRange(self.selection_range.get_start(), self.cursor_location.copy()))
            else:
                self.cursor_location.set_line(self.cursor_location.get_line() - 1)
                self.cursor_location.set_column(len(self.lines[self.cursor_location.get_line()]))
                if shift:
                    if not self.selection_range:
                        self.set_selection_range(LocationRange(previous, self.cursor_location.copy()))
                    else:
                        self.set_selection_range(LocationRange(self.selection_range.get_start(), self.cursor_location.copy()))

        if not shift:
            self.set_selection_range(None)
        self.notify_cursor_observers()

    def move_cursor_right(self, shift: bool = False, ctrl: bool = False):
        previous = self.cursor_location.copy()
        line = self.lines[self.cursor_location.get_line()]
        if ctrl:
            if self.cursor_location.get_column() < len(line):
                boundary = StringUtils.find_word_boundary_right(line, self.cursor_location.get_column())
                self.cursor_location.set_column(boundary)
            elif self.cursor_location.get_line() < len(self.lines) - 1:
                self.cursor_location.set_line(self.cursor_location.get_line() + 1)
                self.cursor_location.set_column(0)
            # else: already at end of document, do nothing
            if shift:
                if not self.selection_range:
                    self.set_selection_range(LocationRange(previous, self.cursor_location.copy()))
                else:
                    self.set_selection_range(LocationRange(self.selection_range.get_start(), self.cursor_location.copy()))
        else:
            if self.cursor_location.get_column() < len(line):
                self.cursor_location.set_column(self.cursor_location.get_column() + 1)
            elif self.cursor_location.get_line() < len(self.lines) - 1:
                self.cursor_location.set_line(self.cursor_location.get_line() + 1)
                self.cursor_location.set_column(0)
            # else: already at end of document, do nothing
            if shift:
                if not self.selection_range:
                    self.set_selection_range(LocationRange(previous, self.cursor_location.copy()))
                else:
                    self.set_selection_range(LocationRange(self.selection_range.get_start(), self.cursor_location.copy()))
        if not shift:
            self.set_selection_range(None)
        self.notify_cursor_observers()

    def move_cursor_up(self, shift: bool = False):
        previous = self.cursor_location.copy()
        if self.cursor_location.get_line() > 0:
            self.cursor_location.set_line(self.cursor_location.get_line() - 1)
            if self.cursor_location.get_column() > len(self.lines[self.cursor_location.get_line()]):
                self.cursor_location.set_column(len(self.lines[self.cursor_location.get_line()]))
            if shift:
                if not self.selection_range:
                    self.set_selection_range(LocationRange(previous, self.cursor_location.copy()))
                else:
                    self.set_selection_range(LocationRange(self.selection_range.get_start(), self.cursor_location.copy()))
            else:
                self.set_selection_range(None)
        else:
            if not shift:
                self.set_selection_range(None)
        self.notify_cursor_observers()

    def move_cursor_down(self, shift: bool = False):
        previous = self.cursor_location.copy()
        if self.cursor_location.get_line() < len(self.lines) - 1:
            self.cursor_location.set_line(self.cursor_location.get_line() + 1)
            if self.cursor_location.get_column() > len(self.lines[self.cursor_location.get_line()]):
                self.cursor_location.set_column(len(self.lines[self.cursor_location.get_line()]))
            if shift:
                if not self.selection_range:
                    self.set_selection_range(LocationRange(previous, self.cursor_location.copy()))
                else:
                    self.set_selection_range(LocationRange(self.selection_range.get_start(), self.cursor_location.copy()))
            else:
                self.set_selection_range(None)
        else:
            if not shift:
                self.set_selection_range(None)
        self.notify_cursor_observers()

    # Returns deleted text and the range of the deletion (for command history)
    def delete_before(self, ctrl: bool = False) -> tuple[str, LocationRange]:
        if self.selection_range:
            return self.delete_range()
        
        if ctrl:
            if self.cursor_location.get_column() > 0:
                boundary = StringUtils.find_word_boundary_left(self.lines[self.cursor_location.get_line()], self.cursor_location.get_column())
                selection = LocationRange(Location(self.cursor_location.get_line(), boundary), self.cursor_location.copy())
                return self.delete_range(selection)
            elif self.cursor_location.get_line() > 0:
                prev_line = self.lines[self.cursor_location.get_line() - 1]
                current_line = self.lines[self.cursor_location.get_line()]
                boundary = StringUtils.find_word_boundary_left(prev_line, len(prev_line))
                selection = LocationRange(Location(self.cursor_location.get_line() - 1, boundary), Location(self.cursor_location.get_line(), 0))
                return self.delete_range(selection)
        
        if self.cursor_location.get_column() > 0:
            line = self.lines[self.cursor_location.get_line()]
            deleted_text = line[self.cursor_location.get_column() - 1]
            location_left = Location(self.cursor_location.get_line(), self.cursor_location.get_column() - 1)
            range = LocationRange(location_left, self.cursor_location.copy())
            line = self.lines[self.cursor_location.get_line()]
            self.lines[self.cursor_location.get_line()] = line[:self.cursor_location.get_column() - 1] + line[self.cursor_location.get_column():]
            self.cursor_location.set_column(self.cursor_location.get_column() - 1)
            self.notify_text_observers(self.cursor_location.get_line(), self.cursor_location.get_line() + 1)    # Change in the same line
            self.notify_cursor_observers()
            return (deleted_text, range)

        elif self.cursor_location.get_line() > 0:
            location1 = Location(self.cursor_location.get_line() - 1, len(self.lines[self.cursor_location.get_line() - 1]))
            location2 = Location(self.cursor_location.get_line(), 0)
            range = LocationRange(location1, location2)
            prev_line = self.lines[self.cursor_location.get_line() - 1]
            current_line = self.lines[self.cursor_location.get_line()]
            self.lines[self.cursor_location.get_line() - 1] = prev_line + current_line
            del self.lines[self.cursor_location.get_line()]
            self.cursor_location.set_line(self.cursor_location.get_line() - 1)
            self.cursor_location.set_column(len(prev_line))
            self.notify_text_observers(self.cursor_location.get_line() - 1, -1)   # Change from line above to the end
            self.notify_cursor_observers()
            return ("\n", range)
        
        else:
            return (None, None)

    # Returns deleted text and the range of the deletion (for command history)
    def delete_after(self, ctrl: bool = False) -> tuple[str, LocationRange]:
        if self.selection_range:
            return self.delete_range()

        if ctrl:
            if self.cursor_location.get_column() < len(self.lines[self.cursor_location.get_line()]):
                boundary = StringUtils.find_word_boundary_right(self.lines[self.cursor_location.get_line()], self.cursor_location.get_column())
                selection = LocationRange(self.cursor_location.copy(), Location(self.cursor_location.get_line(), boundary))
                return self.delete_range(selection)
            elif self.cursor_location.get_line() < len(self.lines) - 1:
                boundary = StringUtils.find_word_boundary_right(self.lines[self.cursor_location.get_line() + 1], 0)
                selection = LocationRange(self.cursor_location.copy(), Location(self.cursor_location.get_line() + 1, boundary))
                return self.delete_range(selection)
        
        line = self.lines[self.cursor_location.get_line()]
        if self.cursor_location.get_column() < len(line):
            deleted_text = line[self.cursor_location.get_column()]
            location_right = Location(self.cursor_location.get_line(), self.cursor_location.get_column() + 1)
            range = LocationRange(location_right, self.cursor_location.copy())
            self.lines[self.cursor_location.get_line()] = line[:self.cursor_location.get_column()] + line[self.cursor_location.get_column() + 1:]
            self.notify_text_observers(self.cursor_location.get_line(), self.cursor_location.get_line() + 1)    # Change in the same line
            self.notify_cursor_observers()
            return (deleted_text, range)

        elif self.cursor_location.get_line() < len(self.lines) - 1:
            range = LocationRange(self.cursor_location.copy(), self.cursor_location.copy())
            next_line = self.lines[self.cursor_location.get_line() + 1]
            self.lines[self.cursor_location.line] = line + next_line
            del self.lines[self.cursor_location.get_line() + 1]
            self.notify_text_observers(self.cursor_location.get_line(), -1)    # Change from current line to the end
            self.notify_cursor_observers()
            return ("\n", range)
        
        else:
            return (None, None)

    # Returns deleted text and the range of the deletion (for command history)
    def delete_range(self, range: LocationRange = None) -> tuple[str, LocationRange]:
        if not range:
            range = self.get_selection_range().copy()
        if not range:
            return (None, None)
        
        range_temp = self.selection_range.copy() if self.selection_range else None
        self.selection_range = range
        previous_text = self.copy()
        self.selection_range = range_temp
        
        start, end = sorted([range.get_start(), range.get_end()])
        
        if start.get_line() == end.get_line():
            line = self.lines[start.get_line()]
            self.lines[start.get_line()] = line[:start.get_column()] + line[end.get_column():]
            self.notify_text_observers(start.get_line(), start.get_line() + 1)  # Change in the same line
        else:
            first_line = self.lines[start.get_line()]
            last_line = self.lines[end.get_line()]
            self.lines[start.get_line()] = first_line[:start.get_column()] + last_line[end.get_column():]
            del self.lines[start.get_line() + 1:end.get_line() + 1]
            self.notify_text_observers(start.get_line(), -1)    # Change from start line to the end of the last line
        self.cursor_location = Location(start.get_line(), start.get_column())

        self.set_selection_range(None)
        self.notify_cursor_observers()

        return (previous_text, range)
    
    # Returns the overwritten text with the range of the old text and the new text with the range of the new text (for command history)
    def insert(self, text: str) -> tuple[str, LocationRange, str, LocationRange]:
        previous_text = ""
        previous_range = LocationRange(self.cursor_location.copy(), self.cursor_location.copy())
        new_text_start = self.cursor_location.copy()

        if self.selection_range:
            new_text_start = min(self.selection_range.get_start(), self.selection_range.get_end())
            previous_text = self.copy()
            previous_range = self.selection_range.copy()
            self.delete_range()

        lines = text.split("\n")    # Using splitlines() would not work correctly
        if len(lines) == 1:
            line = self.lines[self.cursor_location.get_line()]
            self.lines[self.cursor_location.get_line()] = line[:self.cursor_location.get_column()] + lines[0] + line[self.cursor_location.get_column():]
            self.cursor_location.set_column(self.cursor_location.get_column() + len(lines[0]))
            self.notify_text_observers(self.cursor_location.get_line(), self.cursor_location.get_line() + 1)
        else:
            first_line = lines[0]
            last_line = lines[-1]
            cursor = self.cursor_location.copy()
            line, col = cursor.get_line(), cursor.get_column()
            before = self.lines[line][:col]
            after = self.lines[line][col:]
            self.lines[line] = before + first_line  # First line
            self.lines[line + 1:line + 1] = [last_line + after] # Last line
            self.lines[line + 1:line + 1] = lines[1:-1] # Insert middle lines
            new_location = Location(line + len(lines) - 1, len(last_line))
            self.cursor_location = new_location
            self.notify_text_observers(line, -1)
        self.notify_cursor_observers()

        new_range = LocationRange(new_text_start, self.cursor_location.copy())

        return (previous_text, previous_range, text, new_range)

    def copy(self) -> str:
        if not self.selection_range:
            return ""
        
        start, end = sorted([self.selection_range.get_start(), self.selection_range.get_end()])
        
        if start.get_line() == end.get_line():
            return self.lines[start.get_line()][start.get_column():end.get_column()]
        
        result = []
        result.append(self.lines[start.get_line()][start.get_column():])
        for line in range(start.get_line() + 1, end.get_line()):
            result.append(self.lines[line])
        result.append(self.lines[end.get_line()][:end.get_column()])
        
        return "\n".join(result)
    
    # Returns the cut text and the range of the deletion (for command history)
    def cut(self) -> tuple[str, LocationRange]:
        if not self.selection_range:
            return (None, None)
        
        text = self.copy()
        range = self.selection_range.copy()
        self.delete_range()
        return (text, range)