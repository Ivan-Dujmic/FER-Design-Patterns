from __future__ import annotations
from abc import ABC, abstractmethod
from point import Point
from rectangle import Rectangle

class Renderer(ABC):
    @abstractmethod
    def draw_line(self, point1: Point, point2: Point):
        pass

    @abstractmethod
    def fill_polygon(self, points: list[Point]):
        pass

    @abstractmethod
    def draw_rectangle(self, rectangle: Rectangle, color: str):
        pass