from __future__ import annotations
from abc import ABC, abstractmethod
from point import Point
from renderer import Renderer
from graphical_object import GraphicalObject

class State(ABC):
    @abstractmethod
    def mouse_down(self, mouse_point: Point, shift_down: bool, ctrl_down: bool):
        pass

    @abstractmethod
    def mouse_up(self, mouse_point: Point, shift_down: bool, ctrl_down: bool):
        pass

    @abstractmethod
    def mouse_dragged(self, mouse_point: Point):
        pass

    @abstractmethod
    def key_pressed(self, key_code: int):
        pass

    # Called after the canvas draws the passed down graphical object or with None when when it draws the whole canvas
    @abstractmethod
    def after_draw(self, renderer: Renderer, graphics_object: GraphicalObject = None):
        pass

    @abstractmethod
    def on_leaving(self):
        pass