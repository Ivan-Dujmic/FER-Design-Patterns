from __future__ import annotations
from renderer import Renderer
from point import Point
from rectangle import Rectangle

class SVGRendererImpl(Renderer):
    def __init__(self, file_name: str, canvas_width: int, canvas_height: int):
        self.file_name = file_name
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

        self.lines: list[str] = []
        self.lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas_width}" height="{canvas_height}">')

    def close(self):
        self.lines.append('</svg>')
        with open(self.file_name, 'w') as file:
            file.write('\n'.join(self.lines))
        
    def draw_line(self, point1: Point, point2: Point, color: str = 'black'):
        line = f'<line x1="{point1.x}" y1="{point1.y}" x2="{point2.x}" y2="{point2.y}" stroke="{color}" />'
        self.lines.append(line)

    def fill_polygon(self, points: list[Point], color_fill: str = 'blue', color_outline: str = 'red'):
        points_str = ' '.join(f'{point.x},{point.y}' for point in points)
        polygon_fill = f'<polygon points="{points_str}" fill="{color_fill}" stroke="none" />'
        polygon_outline = f'<polygon points="{points_str}" fill="none" stroke="{color_outline}" />'
        self.lines.append(polygon_fill)
        self.lines.append(polygon_outline)

    def draw_rectangle(self, rectangle: Rectangle, color: str = 'green'):
        rect = f'<rect x="{rectangle.x}" y="{rectangle.y}" width="{rectangle.width}" height="{rectangle.height}" fill="none" stroke="{color}" />'
        self.lines.append(rect)