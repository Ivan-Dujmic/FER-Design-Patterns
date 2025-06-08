from __future__ import annotations
from .plugin import Plugin
from tkinter import filedialog, messagebox
import re

class statistics_plugin(Plugin):
    def get_name(self) -> str:
        return "Statistics"

    def get_description(self) -> str:
        return "Shows row, word and character count in a dialog."

    def execute(self, editor = None):
        lines = editor.get_model().get_lines()
        row_count = len(lines)
        word_count = sum(len(re.findall(r'\b\w+\b', line)) for line in lines)
        char_count = sum(len(line) for line in lines)
        message = (
            f"Row count: {row_count}\n"
            f"Word count: {word_count}\n"
            f"Character count: {char_count}"
        )
        messagebox.showinfo("Statistics", message)