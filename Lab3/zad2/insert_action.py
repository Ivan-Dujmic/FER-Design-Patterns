from edit_action import EditAction
from text_editor_model import TextEditorModel
from location import Location
from location_range import LocationRange

class InsertAction(EditAction):
    def __init__(self, model: TextEditorModel, prev_text: str, prev_location_range: LocationRange, new_text: str, new_location_range: LocationRange):
        self.model = model
        self.prev_text = prev_text
        self.prev_location_range = prev_location_range
        self.new_text = new_text
        self.new_location_range = new_location_range

    def execute_do(self):
        self.model.set_selection_range(self.prev_location_range)
        self.model.insert(self.new_text)
        self.model.set_cursor_location(self.new_location_range.get_end())

    def execute_undo(self):
        self.model.set_selection_range(self.new_location_range)
        self.model.insert(self.prev_text)
        self.model.set_cursor_location(self.prev_location_range.get_end())