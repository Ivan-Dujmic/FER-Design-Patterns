from __future__ import annotations
from state import State
from point import Point
from renderer import Renderer
from graphical_object import GraphicalObject

class IdleState(State):
    def mouse_down(self, mouse_point: Point, shift_down: bool, ctrl_down: bool):
        pass

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