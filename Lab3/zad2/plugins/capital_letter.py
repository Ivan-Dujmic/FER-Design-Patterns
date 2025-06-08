from __future__ import annotations
from .plugin import Plugin
import re

class capital_letter(Plugin):
    def get_name(self) -> str:
        return "Capital Letter"

    def get_description(self) -> str:
        return "Converts the first letter of each word to uppercase."

    def execute(self, editor = None):
        if editor is None:
            return
        
        lines = editor.get_model().get_lines()
        modified_lines = []
        
        for line in lines:
            modified_line = ' '.join(word.capitalize() for word in line.split())
            modified_lines.append(modified_line)
        
        editor.clear()
        editor.get_model().insert('\n'.join(modified_lines))