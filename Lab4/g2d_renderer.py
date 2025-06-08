from __future__ import annotations
from renderer import Renderer
from tkinter import Canvas
from point import Point
from rectangle import Rectangle

class G2DRenderer(Renderer):
    def __init__(self, canvas: Canvas):
        self.canvas: Canvas = canvas

    def draw_line(self, point1: Point, point2: Point, color: str = 'black'):
        self.canvas.create_line(point1.get_x(), point1.get_y(), point2.get_x(), point2.get_y(), fill=color, width=2)

    def fill_polygon(self, points: list[Point], color_fill: str = 'blue', color_outline: str = 'red'):
        flat_points = [coord for point in points for coord in (point.get_x(), point.get_y())]
        self.canvas.create_polygon(flat_points, fill=color_fill, outline='')
        self.canvas.create_polygon(flat_points, fill='', outline=color_outline)

    def draw_rectangle(self, rectangle: Rectangle, color: str = 'green'):
        x1 = rectangle.get_x()
        y1 = rectangle.get_y()
        x2 = rectangle.get_x() + rectangle.get_width()
        y2 = rectangle.get_y() + rectangle.get_height()
        self.canvas.create_rectangle(x1, y1, x2, y2, outline=color, width=1)