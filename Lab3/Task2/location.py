from __future__ import annotations

class Location:
    def __init__(self, line: int, column: int):
        self.line: int = line
        self.column: int = column

    def copy(self) -> Location:
        return Location(self.line, self.column)

    def __lt__(self, other: Location) -> bool:
        return (self.line, self.column) < (other.line, other.column)

    def __eq__(self, other: Location) -> bool:
        return (self.line, self.column) == (other.line, other.column)
    
    def get_line(self) -> int:
        return self.line
    
    def set_line(self, line: int):
        self.line = line
    
    def get_column(self) -> int:
        return self.column

    def set_column(self, column: int):
        self.column = column