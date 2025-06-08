from __future__ import annotations
from state import State
from document_model import DocumentModel
from point import Point
from renderer import Renderer
from graphical_object import GraphicalObject
from renderer import Renderer
from free_line import FreeLine

class EraserState(State):
    def __init__(self, model: DocumentModel):
        self.model = model
        self.line = None

    def mouse_down(self, mouse_point: Point, shift_down: bool, ctrl_down: bool):
        self.line = FreeLine(mouse_point)
        self.model.add_graphical_object(self.line)

    def mouse_dragged(self, mouse_point: Point):
        self.line.add_point(mouse_point)

    def mouse_up(self, mouse_point: Point, shift_down: bool, ctrl_down: bool):
        self.line.add_point(mouse_point)
        if self.line is not None:
            self.model.remove_graphical_object(self.line)
            proximity = self.model.get_proximity()
            for point in self.line.hot_points:
                for obj in self.model.get_list():
                    if obj.selection_distance(point) <= proximity:
                        self.model.remove_graphical_object(obj)
                self.line = None

    def key_pressed(self, key_code: int):
        pass

    def after_draw(self, renderer: Renderer, graphics_object: GraphicalObject = None):
        pass

    def on_leaving(self):
        self.line = None