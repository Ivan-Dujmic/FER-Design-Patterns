from __future__ import annotations
from abstract_graphical_object import AbstractGraphicalObject
from geometry_util import GeometryUtil
from point import Point
from rectangle import Rectangle
from graphical_object import GraphicalObject
from renderer import Renderer
from collections import deque
from document_model import DocumentModel
from math import cos, sin, pi as PI

class Oval(AbstractGraphicalObject):
    NUMBER_OF_LINE_SEGMENTS = 90

    def __init__(self, point_right: Point = Point(10, 0), point_down: Point = Point(0, 10)):
        super().__init__([point_right, point_down])

    def get_bounding_box(self) -> Rectangle:
        # We know that the first point is the rightmost and the second point is the bottommost
        x = 2 * self.hot_points[1].get_x() - self.hot_points[0].get_x()
        y = 2 * self.hot_points[0].get_y() - self.hot_points[1].get_y()
        width = self.hot_points[0].get_x() - x
        height = self.hot_points[1].get_y() - y
        return Rectangle(x, y, width, height)

    def selection_distance(self, mouse_point: Point) -> float:
        rightmost = self.hot_points[0]
        bottommost = self.hot_points[1]

        center = Point(bottommost.get_x(), rightmost.get_y())

        # Radii
        rx = rightmost.get_x() - center.get_x()
        ry = bottommost.get_y() - center.get_y()

        # If the radii are zero, it means the oval is actually a point
        if rx == 0 and ry == 0:
            return GeometryUtil.distance_from_point(center, mouse_point)

        # If one of the radii is zero, it means the oval is actually a line segment
        if rx == 0:
            return GeometryUtil.distance_from_line_segment(
                Point(center.get_x(), center.get_y() - ry),
                Point(center.get_x(), center.get_y() + ry),
                mouse_point
            )
        if ry == 0:
            return GeometryUtil.distance_from_line_segment(
                Point(center.get_x() - rx, center.get_y()),
                Point(center.get_x() + rx, center.get_y()),
                mouse_point
            )

        # Translate mouse point relative to center
        delta = mouse_point.difference(center)

        # Check if point is inside the oval
        dx = delta.get_x() / rx
        dy = delta.get_y() / ry
        if dx * dx + dy * dy <= 1:
            return 0.0  # Point is inside the filled oval

        # Normalize
        delta_norm = Point(dx, dy)

        # Closest point on ellipse boundary in normalized space
        length = GeometryUtil.distance_from_point(Point(0, 0), delta_norm)
        if length == 0:
            return min(rx, ry)

        nearest_point = Point(
            center.get_x() + delta_norm.get_x() * rx / length,
            center.get_y() + delta_norm.get_y() * ry / length
        )

        return GeometryUtil.distance_from_point(nearest_point, mouse_point)

    def render(self, renderer: Renderer, document_model: DocumentModel, draw_rectangles: bool = True):
        if draw_rectangles:
            super().render(renderer, document_model)

        # Approximate with a polygon using cos and sin from math
        rightmost = self.hot_points[0]
        bottommost = self.hot_points[1]
        center = Point(bottommost.get_x(), rightmost.get_y())
        rx = rightmost.get_x() - center.get_x()
        ry = bottommost.get_y() - center.get_y()

        points = [
            Point(
            center.get_x() + rx * cos(2 * PI * i / self.NUMBER_OF_LINE_SEGMENTS),
            center.get_y() + ry * sin(2 * PI * i / self.NUMBER_OF_LINE_SEGMENTS)
            )
            for i in range(self.NUMBER_OF_LINE_SEGMENTS)
        ]

        renderer.fill_polygon(points)
        for i in range(self.NUMBER_OF_LINE_SEGMENTS):
            renderer.draw_line(points[i], points[(i + 1) % self.NUMBER_OF_LINE_SEGMENTS])

    def get_shape_name(self) -> str:
        return "Oval"

    def duplicate(self) -> GraphicalObject:
        return Oval(self.hot_points[0], self.hot_points[1])

    def get_shape_id(self) -> str:
        return "@OVAL"

    @classmethod
    def load(cls, stack: deque['GraphicalObject'], data: str):
        x1, y1, x2, y2 = map(int, data.split())
        point_right = Point(x1, y1)
        point_down = Point(x2, y2)
        oval = Oval(point_right, point_down)
        stack.append(oval)

    def save(self, rows: list[str]):
        rows.append(f"{self.get_shape_id()} {self.hot_points[0].get_x()} {self.hot_points[0].get_y()} {self.hot_points[1].get_x()} {self.hot_points[1].get_y()}")