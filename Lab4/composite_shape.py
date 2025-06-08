from __future__ import annotations
from graphical_object import GraphicalObject
from point import Point
from rectangle import Rectangle
from renderer import Renderer
from collections import deque
from document_model import DocumentModel
from graphical_object_listener import GraphicalObjectListener

class CompositeShape(GraphicalObject):
    def __init__(self, objects: list[GraphicalObject]):
        self.objects: list[GraphicalObject] = objects
        self.selected: bool = False
        self.listeners: list[GraphicalObjectListener] = []
        self.notify_listeners()

    def get_objects(self) -> list[GraphicalObject]:
        return self.objects

    def is_selected(self) -> bool:
        return self.selected

    def set_selected(self, selected: bool):
        if self.selected != selected:
            self.selected = selected
            self.notify_selection_listeners()

    def get_number_of_hot_points(self) -> int:
        return 0

    def get_hot_point(self, index: int) -> Point:
        raise IndexError("CompositeShape does not have hot points")

    def set_hot_point(self, index: int, point: Point):
        raise IndexError("CompositeShape does not have hot points")

    def is_hot_point_selected(self, index: int) -> bool:
        raise IndexError("CompositeShape does not have hot points")

    def set_hot_point_selected(self, index: int, selected: bool):
        raise IndexError("CompositeShape does not have hot points")

    def get_hot_point_distance(self, index: int, mouse_point: Point) -> float:
        raise IndexError("CompositeShape does not have hot points")

    def translate(self, delta: Point):
        for obj in self.objects:
            obj.translate(delta)
        self.notify_listeners()

    def get_bounding_box(self) -> Rectangle:
        if not self.objects:
            return Rectangle(0, 0, 0, 0)
        
        min_x = min(obj.get_bounding_box().x for obj in self.objects)
        min_y = min(obj.get_bounding_box().y for obj in self.objects)
        max_x = max(obj.get_bounding_box().x + obj.get_bounding_box().width for obj in self.objects)
        max_y = max(obj.get_bounding_box().y + obj.get_bounding_box().height for obj in self.objects)

        return Rectangle(min_x, min_y, max_x - min_x, max_y - min_y)

    def selection_distance(self, mouse_point: Point) -> float:
        distances = [obj.selection_distance(mouse_point) for obj in self.objects]
        return min(distances) if distances else float('inf')

    def render(self, renderer: Renderer, document_model: DocumentModel, draw_rectangles: bool = True):
        for obj in self.objects:
            obj.render(renderer, document_model, False)

        if self.is_selected():
            bounding_box = self.get_bounding_box()
            renderer.draw_rectangle(bounding_box, "green")

    def add_graphical_object_listener(self, listener: GraphicalObjectListener):
        if listener not in self.listeners:
            self.listeners.append(listener)

    def remove_graphical_object_listener(self, listener: GraphicalObjectListener):
        if listener in self.listeners:
            self.listeners.remove(listener)

    def get_shape_name(self) -> str:
        return "Composite"

    def duplicate(self) -> GraphicalObject:
        new_objects = [obj.duplicate() for obj in self.objects]
        return CompositeShape(new_objects)

    def get_shape_id(self) -> str:
        return "@COMP"

    @classmethod
    def load(cls, stack: deque[GraphicalObject], data: str):
        parts = int(data)
        objects = []
        for _ in range(parts):
            obj_data = stack.pop()
            objects.append(obj_data)
        objects.reverse()
        composite_shape = CompositeShape(objects)
        stack.append(composite_shape)

    def save(self, rows: list[str]):
        for obj in self.objects:
            obj.save(rows)
        rows.append(f"{self.get_shape_id()} {len(self.objects)}")

    def document_change(self):
        pass

    def notify_listeners(self):
        for listener in self.listeners:
            listener.graphical_object_changed(self)

    def notify_selection_listeners(self):
        for listener in self.listeners:
            listener.graphical_object_selection_changed(self)