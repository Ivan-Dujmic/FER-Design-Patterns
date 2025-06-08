from __future__ import annotations
from state import State
from graphical_object import GraphicalObject
from document_model import DocumentModel
from point import Point
from renderer import Renderer

class AddShapeState(State):
    def __init__(self, document_model: DocumentModel, prototype: GraphicalObject):
        self.document_model = document_model
        self.prototype = prototype

    def mouse_down(self, mouse_point: Point, shift_down: bool, ctrl_down: bool):
        new_object = self.prototype.duplicate()
        new_object.translate(mouse_point)
        self.document_model.add_graphical_object(new_object)

    def mouse_up(self, mouse_point: Point, shift_down: bool, ctrl_down: bool):
        pass

    def mouse_dragged(self, mouse_point: Point):
        pass

    def key_pressed(self, key_code: int):
        pass

    def after_draw(self, renderer: Renderer, graphics_object: GraphicalObject = None):
        pass

    def on_leaving(self):
        pass
