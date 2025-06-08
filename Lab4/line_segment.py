from __future__ import annotations
from abstract_graphical_object import AbstractGraphicalObject
from geometry_util import GeometryUtil
from point import Point
from rectangle import Rectangle
from graphical_object import GraphicalObject
from renderer import Renderer
from collections import deque
from document_model import DocumentModel

class LineSegment(AbstractGraphicalObject):
    def __init__(self, point1: Point = Point(0, 0), point2: Point = Point(10, 0)):
        super().__init__([point1, point2])

    def get_bounding_box(self) -> Rectangle:
        x = min(self.hot_points[0].get_x(), self.hot_points[1].get_x())
        y = min(self.hot_points[0].get_y(), self.hot_points[1].get_y())
        width = abs(self.hot_points[1].get_x() - self.hot_points[0].get_x())
        height = abs(self.hot_points[1].get_y() - self.hot_points[0].get_y())
        return Rectangle(x, y, width, height)

    def selection_distance(self, mouse_point: Point) -> float:
        return GeometryUtil.distance_from_line_segment(self.hot_points[0], self.hot_points[1], mouse_point)

    def render(self, renderer: Renderer, document_model: DocumentModel, draw_rectangles: bool = True):
        if draw_rectangles:
            super().render(renderer, document_model, True)
        renderer.draw_line(self.hot_points[0], self.hot_points[1])

    def get_shape_name(self) -> str:
        return "Line"

    def duplicate(self) -> GraphicalObject:
        return LineSegment(self.hot_points[0], self.hot_points[1])

    def get_shape_id(self) -> str:
        return "@LINE"

    @classmethod
    def load(cls, stack: deque[GraphicalObject], data: str):
        x1, y1, x2, y2 = map(int, data.split())
        point1 = Point(x1, y1)
        point2 = Point(x2, y2)
        line_segment = LineSegment(point1, point2)
        stack.append(line_segment)

    def save(self, rows: list[str]):
        rows.append(f"{self.get_shape_id()} {self.hot_points[0].get_x()} {self.hot_points[0].get_y()} {self.hot_points[1].get_x()} {self.hot_points[1].get_y()}")