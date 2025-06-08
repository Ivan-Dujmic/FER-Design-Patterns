from __future__ import annotations

class Point():
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
    
    def get_x(self) -> int:
        return self.x
    
    def get_y(self) -> int:
        return self.y
    
    def translate(self, dx: int, dy: int) -> Point:
        return Point(self.x + dx, self.y + dy)
    
    def difference(self, other: 'Point') -> Point:
        return Point(self.x - other.x, self.y - other.y)