from __future__ import annotations
from abstract_graphical_object import AbstractGraphicalObject
from geometry_util import GeometryUtil
from point import Point
from rectangle import Rectangle
from graphical_object import GraphicalObject
from renderer import Renderer
from collections import deque
from document_model import DocumentModel

class FreeLine(AbstractGraphicalObject):
    def __init__(self, start_point: Point):
        super().__init__([start_point])

    def add_point(self, point: Point):
        self.hot_points.append(point)
        self.notify_listeners()

    def get_bounding_box(self) -> Rectangle:
        return Rectangle(0, 0, 0, 0)

    def selection_distance(self, mouse_point: Point) -> float:
        return float('inf')

    def render(self, renderer: Renderer, document_model: DocumentModel, draw_rectangles: bool = False):
        for i in range(len(self.hot_points) - 1):
            renderer.draw_line(self.hot_points[i], self.hot_points[i + 1], "red")

    def get_shape_name(self) -> str:
        return "Line"

    def duplicate(self) -> GraphicalObject:
        return FreeLine(self.hot_points[0])

    def get_shape_id(self) -> str:
        pass

    def load(self, stack: deque[GraphicalObject], data: str):
        pass

    def save(self, rows: list[str]):
        pass