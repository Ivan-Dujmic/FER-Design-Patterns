from __future__ import annotations
from location import Location

class LocationRange:
    def __init__(self, start: Location, end: Location):
        self.start: Location = start
        self.end: Location = end

    def copy(self) -> LocationRange:
        return LocationRange(self.start.copy(), self.end.copy())
    
    def get_start(self) -> Location:
        return self.start
    
    def get_end(self) -> Location:
        return self.end