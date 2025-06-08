from __future__ import annotations
from abc import ABC, abstractmethod
from geometry_util import GeometryUtil
from graphical_object import GraphicalObject
from point import Point
from rectangle import Rectangle
from graphical_object_listener import GraphicalObjectListener
from renderer import Renderer
from collections import deque
from document_model import DocumentModel

class AbstractGraphicalObject(GraphicalObject, ABC):
    def __init__(self, hot_points: list[Point]):
        self.hot_points: list[Point] = hot_points
        self.hot_point_selected: list[bool] = [False] * len(hot_points)
        self.selected: bool = False
        self.listeners: list[GraphicalObjectListener] = []

    def get_hot_point(self, index: int) -> Point:
        return self.hot_points[index]
    
    def set_hot_point(self, index: int, point: Point):
        self.hot_points[index] = point
        self.notify_listeners()

    def get_number_of_hot_points(self) -> int:
        return len(self.hot_points)
    
    def get_hot_point_distance(self, index, mouse_point: Point) -> float:
        return GeometryUtil.distance_from_point(self.hot_points[index], mouse_point)
    
    def is_hot_point_selected(self, index: int) -> bool:
        return self.hot_point_selected[index]
    
    def set_hot_point_selected(self, index: int, selected: bool):
        self.hot_point_selected[index] = selected
        self.notify_listeners()

    def is_selected(self) -> bool:
        return self.selected
    
    def set_selected(self, selected: bool):
        if self.selected != selected:
            self.selected = selected
            self.notify_selection_listeners()

    def translate(self, delta: Point):
        for i in range(len(self.hot_points)):
            self.hot_points[i] = self.hot_points[i].translate(delta.get_x(), delta.get_y())
        self.notify_listeners()

    def add_graphical_object_listener(self, listener: GraphicalObjectListener):
        if listener not in self.listeners:
            self.listeners.append(listener)

    def remove_graphical_object_listener(self, listener: GraphicalObjectListener):
        if listener in self.listeners:
            self.listeners.remove(listener)

    def notify_listeners(self):
        for listener in self.listeners:
            listener.graphical_object_changed(self)

    def notify_selection_listeners(self):
        for listener in self.listeners:
            listener.graphical_object_selection_changed(self)

    def document_change(self):
        pass

    @abstractmethod
    def get_bounding_box(self) -> Rectangle:
        pass

    @abstractmethod
    def selection_distance(self, mouse_point: Point) -> float:
        pass

    # Abstract renders the bounding_box and hot_points if it's the only selected object
    # but subclasses should implement their own rendering logic for the shape itself and call super().render(renderer)
    @abstractmethod
    def render(self, renderer: Renderer, document_model: DocumentModel, draw_rectangles: bool = True):
        if not self.is_selected():
            return
        bounding_box = self.get_bounding_box()
        renderer.draw_rectangle(bounding_box, "green")
        
        if document_model.get_number_of_selected_objects() == 1 and self.is_selected():
            for point in self.hot_points:
                rectangle = Rectangle(point.get_x() - 3, point.get_y() - 3, 6, 6)
                renderer.draw_rectangle(rectangle, "red")

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
    def load(cls, stack: deque['GraphicalObject'], data: str):
        pass

    @abstractmethod
    def save(self, rows: list[str]):
        pass