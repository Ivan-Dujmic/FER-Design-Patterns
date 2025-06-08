from __future__ import annotations
from typing import TYPE_CHECKING
from graphical_object_listener import GraphicalObjectListener
from document_model_listener import DocumentModelListener
from point import Point
from read_only_list import ReadOnlyList

if TYPE_CHECKING:
    from graphical_object import GraphicalObject

class DocumentModel(GraphicalObjectListener):
    SELECTION_PROXIMITY = 10

    def __init__(self):
        self.objects: list[GraphicalObject] = []
        self.ro_objects: ReadOnlyList = ReadOnlyList(self.objects)
        self.listeners: list[DocumentModelListener] = []
        self.selected_objects: list[GraphicalObject] = []
        self.ro_selected_objects: ReadOnlyList = ReadOnlyList(self.selected_objects)
        
    def clear(self):
        for graphical_object in self.objects:
            graphical_object.remove_graphical_object_listener(self)
        self.objects.clear()
        self.selected_objects.clear()
        self.notify_listeners()

    def add_graphical_object(self, graphical_object: GraphicalObject):
        if graphical_object not in self.objects:
            self.objects.append(graphical_object)
            if graphical_object.is_selected():
                if graphical_object not in self.selected_objects:
                    self.selected_objects.append(graphical_object)
            graphical_object.add_graphical_object_listener(self)
            self.notify_listeners()

    def remove_graphical_object(self, graphical_object: GraphicalObject):
        if graphical_object in self.objects:
            self.objects.remove(graphical_object)
            if graphical_object in self.selected_objects:
                self.selected_objects.remove(graphical_object)
            graphical_object.remove_graphical_object_listener(self)
            self.notify_listeners()

    def get_list(self) -> tuple[GraphicalObject, ...]:
        return self.ro_objects
    
    def get_proximity(self) -> int:
        return self.SELECTION_PROXIMITY
    
    def add_document_model_listener(self, listener: DocumentModelListener):
        if listener not in self.listeners:
            self.listeners.append(listener)

    def remove_document_model_listener(self, listener: DocumentModelListener):
        if listener in self.listeners:
            self.listeners.remove(listener)

    def notify_listeners(self):
        for listener in self.listeners:
            listener.document_change()

    def get_selected_objects(self) -> tuple[GraphicalObject, ...]:
        return self.ro_selected_objects
    
    def get_number_of_selected_objects(self) -> int:
        return len(self.selected_objects)
    
    # First object in the list is the one with the highest index in self.objects
    def increase_z(self, graphical_object: GraphicalObject):
        if graphical_object in self.objects:
            index = self.objects.index(graphical_object)
            if index < len(self.objects) - 1:
                self.objects[index], self.objects[index + 1] = self.objects[index + 1], self.objects[index]
            self.notify_listeners()

    # Last object in the list is the one with the lowest index in self.objects
    def decrease_z(self, graphical_object: GraphicalObject):
        if graphical_object in self.objects:
            index = self.objects.index(graphical_object)
            if index > 0:
                self.objects[index], self.objects[index - 1] = self.objects[index - 1], self.objects[index]
            self.notify_listeners()

    def find_selected_graphical_object(self, mouse_point: Point) -> GraphicalObject | None:
        closest_distance = float('inf')
        closest_object = None
        for graphical_object in reversed(self.objects):
            distance = graphical_object.selection_distance(mouse_point)
            if distance < closest_distance:
                closest_distance = distance
                closest_object = graphical_object
        if closest_distance < self.SELECTION_PROXIMITY:
            return closest_object
        return None
    
    def find_selected_hot_point(self, graphical_object: GraphicalObject, mouse_point: Point) -> int:
        closest_distance = float('inf')
        closest_index = -1
        for i in range(graphical_object.get_number_of_hot_points()):
            distance = graphical_object.get_hot_point_distance(i, mouse_point)
            if distance < closest_distance:
                closest_distance = distance
                closest_index = i
        if closest_distance < self.SELECTION_PROXIMITY:
            return closest_index
        return -1

    def graphical_object_changed(self, graphical_object: GraphicalObject):
        self.notify_listeners()

    def graphical_object_selection_changed(self, graphical_object: GraphicalObject):
        if graphical_object.is_selected():
            if graphical_object not in self.selected_objects:
                self.selected_objects.append(graphical_object)
        else:
            if graphical_object in self.selected_objects:
                self.selected_objects.remove(graphical_object)
        self.notify_listeners()