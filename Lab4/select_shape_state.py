from __future__ import annotations
from state import State
from point import Point
from renderer import Renderer
from graphical_object import GraphicalObject
from document_model import DocumentModel
from composite_shape import CompositeShape

class SelectShapeState(State):
    def __init__(self, model: DocumentModel):
        self.model = model

    def mouse_down(self, mouse_point: Point, shift_down: bool, ctrl_down: bool):
        found_index = False
        if self.model.get_number_of_selected_objects() == 1:
            obj = self.model.get_selected_objects()[0]
            hot_point_index = self.model.find_selected_hot_point(obj, mouse_point)
            if hot_point_index != -1:
                found_index = True
                if not obj.is_hot_point_selected(hot_point_index):
                    for o in self.model.get_selected_objects():
                        for i in range(o.get_number_of_hot_points()):
                            o.set_hot_point_selected(i, False)
                    obj.set_hot_point_selected(hot_point_index, True)
            elif not ctrl_down:
                obj.set_selected(False)
        if not found_index:
            obj = self.model.find_selected_graphical_object(mouse_point)
            if obj is not None:
                if ctrl_down:
                    obj.set_selected(not obj.is_selected())
                else:
                    for o in self.model.get_selected_objects():
                        o.set_selected(False)
                    obj.set_selected(True)
            else:
                if not ctrl_down:
                    for o in self.model.get_selected_objects():
                        o.set_selected(False)

    def mouse_up(self, mouse_point: Point, shift_down: bool, ctrl_down: bool):
        obj = self.model.get_selected_objects()[0] if self.model.get_selected_objects() else None
        if obj is not None:
            hot_point_index = self.model.find_selected_hot_point(obj, mouse_point)
            if hot_point_index >= 0:
                obj.set_hot_point_selected(hot_point_index, False)
            else:
                if not ctrl_down:
                    for o in self.model.get_selected_objects():
                        o.set_selected(False)
                obj.set_selected(True)

    def mouse_dragged(self, mouse_point: Point):
        selected_objects = self.model.get_selected_objects()
        if len(selected_objects) == 1:
            obj = selected_objects[0]
            hot_point_count = obj.get_number_of_hot_points()
            for i in range(hot_point_count):
                if obj.is_hot_point_selected(i):
                    obj.set_hot_point(i, mouse_point)
                    break

    def key_pressed(self, key_code: int):
        if key_code == 37:  # Left arrow
            for obj in self.model.get_selected_objects():
                obj.translate(Point(-1, 0))
        elif key_code == 38:  # Up arrow
            for obj in self.model.get_selected_objects():
                obj.translate(Point(0, -1))
        elif key_code == 39:  # Right arrow
            for obj in self.model.get_selected_objects():
                obj.translate(Point(1, 0))
        elif key_code == 40:  # Down arrow
            for obj in self.model.get_selected_objects():
                obj.translate(Point(0, 1))
        elif key_code == 107 or key_code == 187:    # Plus key
            if self.model.get_number_of_selected_objects() == 1:
                obj = self.model.get_selected_objects()[0]
                self.model.increase_z(obj)
        elif key_code == 109 or key_code == 189:    # Minus key
            if self.model.get_number_of_selected_objects() == 1:
                obj = self.model.get_selected_objects()[0]
                self.model.decrease_z(obj)
        elif key_code == ord('g') or key_code == ord('G'):
            unsorted_objects = self.model.get_selected_objects()
            objects = sorted(unsorted_objects, key=lambda obj: self.model.get_list().index(obj))
            if len(objects) > 1:
                composite = CompositeShape(objects)
                self.model.add_graphical_object(composite)
                composite.set_selected(True)
                for obj in objects:
                    obj.set_selected(False)
                    self.model.remove_graphical_object(obj)
        elif key_code == ord('u') or key_code == ord('U'):
            if self.model.get_number_of_selected_objects() == 1:
                obj = self.model.get_selected_objects()[0]
                if isinstance(obj, CompositeShape):
                    for sub_obj in obj.get_objects():
                        sub_obj.set_selected(True)
                    obj.set_selected(False)
                    self.model.remove_graphical_object(obj)
                    for sub_obj in obj.objects:
                        self.model.add_graphical_object(sub_obj)

    def after_draw(self, renderer: Renderer, graphics_object: GraphicalObject = None):
        pass

    def on_leaving(self):
        for obj in self.model.get_selected_objects():
            obj.set_selected(False)