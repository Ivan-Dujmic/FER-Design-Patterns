from edit_action import EditAction
from text_editor_model import TextEditorModel
from location import Location
from location_range import LocationRange

class DeleteAction(EditAction):
    def __init__(self, model: TextEditorModel, prev_text: str, location_range: LocationRange):
        self.model = model
        self.prev_text = prev_text
        self.location_range = location_range

    def execute_do(self):
        self.model.delete_range(self.location_range)

    def execute_undo(self):
        start = self.location_range.get_start().copy()
        end = self.location_range.get_end().copy()
        start = min(start, end)
        self.model.set_cursor_location(start)   # Always insert at the start
        self.model.insert(self.prev_text)
        self.model.set_cursor_location(end) # But move the cursor to where it was before (because the text could be deleted with backspace or delete)