from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from point import Point
from rectangle import Rectangle
from renderer import Renderer
from document_model_listener import DocumentModelListener
from collections import deque
from document_model import DocumentModel

if TYPE_CHECKING:
    from graphical_object_listener import GraphicalObjectListener

class GraphicalObject(DocumentModelListener):
    @abstractmethod
    def is_selected(self) -> bool:
        pass

    @abstractmethod
    def set_selected(self, selected: bool):
        pass

    @abstractmethod
    def get_number_of_hot_points(self) -> int:
        pass

    @abstractmethod
    def get_hot_point(self, index: int) -> Point:
        pass

    @abstractmethod
    def set_hot_point(self, index: int, point: Point):
        pass

    @abstractmethod
    def is_hot_point_selected(self, index: int) -> bool:
        pass

    @abstractmethod
    def set_hot_point_selected(self, index: int, selected: bool):
        pass

    @abstractmethod
    def get_hot_point_distance(self, index: int, mouse_point: Point) -> float:
        pass

    @abstractmethod
    def translate(self, delta: Point):
        pass

    @abstractmethod
    def get_bounding_box(self) -> Rectangle:
        pass

    @abstractmethod
    def selection_distance(self, mouse_point: Point) -> float:
        pass

    @abstractmethod
    def render(self, renderer: Renderer, document_model: DocumentModel, draw_rectangles: bool = True):
        pass

    @abstractmethod
    def add_graphical_object_listener(self, listener: GraphicalObjectListener):
        pass

    @abstractmethod
    def remove_graphical_object_listener(self, listener: GraphicalObjectListener):
        pass

    @abstractmethod
    def get_shape_name(self) -> str:
        pass

    @abstractmethod
    def duplicate(self) -> GraphicalObject:
        pass

    @abstractmethod
    def get_shape_id(self) -> str:
        pass

    @classmethod
    @abstractmethod
    def load(cls, stack: deque[GraphicalObject], data: str):
        pass

    @abstractmethod
    def save(self, rows: list[str]):
        pass

    @abstractmethod
    def document_change(self):
        pass