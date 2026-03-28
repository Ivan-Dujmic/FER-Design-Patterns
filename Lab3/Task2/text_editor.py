from typing import TYPE_CHECKING
import tkinter as tk
import tkinter.font as tkfont
from tkinter import filedialog, messagebox
from text_editor_model import TextEditorModel
from cursor_observer import CursorObserver
from text_observer import TextObserver
from selection_observer import SelectionObserver
from clipboard_stack import ClipboardStack
from undo_manager import UndoManager
from insert_action import InsertAction
from delete_action import DeleteAction
from menu_item import MenuItem
from menu_item_undo_observer import MenuItemUndoObserver
from menu_item_redo_observer import MenuItemRedoObserver
from menu_item_clipboard_observer import MenuItemClipboardObserver
from menu_item_selection_observer import MenuItemSelectionObserver
from commands.file.open_command import OpenCommand
from commands.file.save_command import SaveCommand
from commands.file.exit_command import ExitCommand
from commands.edit.undo_command import UndoCommand
from commands.edit.redo_command import RedoCommand
from commands.edit.cut_command import CutCommand
from commands.edit.copy_command import CopyCommand
from commands.edit.paste_command import PasteCommand
from commands.edit.paste_and_take_command import PasteAndTakeCommand
from commands.edit.delete_selection_command import DeleteSelectionCommand
from commands.edit.clear_document_command import ClearDocumentCommand
from commands.move.cursor_to_document_start_command import CursorToDocumentStartCommand
from commands.move.cursor_to_document_end_command import CursorToDocumentEndCommand
import os
from importlib import import_module
from plugins.plugin import Plugin

def myfactory(module_name):
    # Dynamically import the module and get the class from it
    return getattr(import_module('plugins.' + module_name), module_name)

class TextEditor(CursorObserver, TextObserver, SelectionObserver):
    CTRL_MASK = 0x0004  # Control key mask for Windows
    SHIFT_MASK = 0x0001  # Shift key mask for Windows

    def __init__(self, model: TextEditorModel):
        self.visible = False
        self.model: TextEditorModel = model

        self.root: tk.Tk = tk.Tk()
        self.root.title("Text Editor")
        self.root.geometry("800x600")

        self.clipboard_stack: ClipboardStack = ClipboardStack()
        self.undo_manager: UndoManager = UndoManager()

        self.x_offset: int = 7
        self.y_offset: int = 5
        self.font: tkfont.Font = tkfont.Font(family="Times New Roman", size=16)
        self.line_height: int = self.font.metrics("linespace")
        self.text_color: str = "white"
        self.bg_color: str = "black"
        self.selection_color: str = "blue"
        self.cursor_color: str = "red"

        self.menu_bar: tk.Menu = tk.Menu(self.root)
        self.set_menu()

        self.canvas: tk.Canvas = tk.Canvas(self.root, bg=self.bg_color, highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.status_bar = tk.Label(self.root, text="", anchor=tk.W, bg="gray80", fg="black", font=("Arial", 10))
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        self.cursor_visible: bool = True
        self.blinking_speed: int = 500  # milliseconds
        self.blinking_id = self.canvas.after(self.blinking_speed, self.blink_cursor)    # Blinking id so we can cancel it later

        self.bind_all()

        self.canvas.focus_set()

        self.model.attach_cursor_observer(self)
        self.model.attach_text_observer(self)
        self.model.attach_selection_observer(self)
        self.redraw_all()

    def set_visible(self, visible: bool):
        self.visible = visible
        if visible:
            self.root.mainloop()
        else:
            self.root.quit()

    def set_menu(self):
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        open_menu_item = MenuItem(OpenCommand(self))
        file_menu.add_command(label="Open", command=open_menu_item.clicked)
        save_menu_item = MenuItem(SaveCommand(self))
        file_menu.add_command(label="Save", command=save_menu_item.clicked)
        file_menu.add_separator()
        exit_menu_item = MenuItem(ExitCommand(self))
        file_menu.add_command(label="Exit", command=exit_menu_item.clicked)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        undo_menu_item = MenuItemUndoObserver(UndoCommand(self), edit_menu, "Undo")
        edit_menu.add_command(label="Undo", command=undo_menu_item.clicked)
        self.undo_manager.attach_observer(undo_menu_item)
        redo_menu_item = MenuItemRedoObserver(RedoCommand(self), edit_menu, "Redo")
        edit_menu.add_command(label="Redo", command=redo_menu_item.clicked)
        self.undo_manager.attach_observer(redo_menu_item)
        edit_menu.add_separator()
        cut_menu_item = MenuItemSelectionObserver(CutCommand(self), edit_menu, "Cut")
        edit_menu.add_command(label="Cut", command=cut_menu_item.clicked)
        self.model.attach_selection_observer(cut_menu_item)
        copy_menu_item = MenuItemSelectionObserver(CopyCommand(self), edit_menu, "Copy")
        edit_menu.add_command(label="Copy", command=copy_menu_item.clicked)
        self.model.attach_selection_observer(copy_menu_item)
        paste_menu_item = MenuItemClipboardObserver(PasteCommand(self), edit_menu, "Paste")
        edit_menu.add_command(label="Paste", command=paste_menu_item.clicked)
        self.clipboard_stack.attach_observer(paste_menu_item)
        paste_and_take_menu_item = MenuItemClipboardObserver(PasteAndTakeCommand(self), edit_menu, "Paste and Take")
        edit_menu.add_command(label="Paste and Take", command=paste_and_take_menu_item.clicked)
        self.clipboard_stack.attach_observer(paste_and_take_menu_item)
        edit_menu.add_separator()
        delete_selection_menu_item = MenuItemSelectionObserver(DeleteSelectionCommand(self), edit_menu, "Delete selection")
        edit_menu.add_command(label="Delete selection", command=delete_selection_menu_item.clicked)
        self.model.attach_selection_observer(delete_selection_menu_item)
        clear_document_menu_item = MenuItem(ClearDocumentCommand(self))
        edit_menu.add_command(label="Clear document", command=clear_document_menu_item.clicked)
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)

        move_menu = tk.Menu(self.menu_bar, tearoff=0)
        cursor_to_start_menu_item = MenuItem(CursorToDocumentStartCommand(self))
        move_menu.add_command(label="Cursor to document start", command=cursor_to_start_menu_item.clicked)
        cursor_to_end_menu_item = MenuItem(CursorToDocumentEndCommand(self))
        move_menu.add_command(label="Cursor to document end", command=cursor_to_end_menu_item.clicked)
        self.menu_bar.add_cascade(label="Move", menu=move_menu)

        plugins_menu = tk.Menu(self.menu_bar, tearoff=0)
        for mymodule in os.listdir('plugins'):
            module_name, module_ext = os.path.splitext(mymodule)
            if module_name == "plugin":
                continue
            if module_ext == '.py':
                plugin = myfactory(module_name)()
                item = MenuItem(plugin, self)
                plugins_menu.add_command(label=plugin.get_name(), command=item.clicked)
        self.menu_bar.add_cascade(label="Plugins", menu=plugins_menu)

        self.root.config(menu=self.menu_bar)

    def update_status_bar(self):
        cursor = self.model.get_cursor_location()
        line = cursor.get_line() + 1
        col = cursor.get_column() + 1
        self.status_bar.config(text=f"Ln: {line}  Col: {col}")

    def bind_all(self):
        self.canvas.bind("<Left>", self.on_left)
        self.canvas.bind("<Right>", self.on_right)
        self.canvas.bind("<Up>", self.on_up)
        self.canvas.bind("<Down>", self.on_down)
        self.canvas.bind("<BackSpace>", self.on_backspace)
        self.canvas.bind("<Delete>", self.on_delete)
        self.canvas.bind("<Return>", self.on_enter)
        self.canvas.bind("<Key>", self.on_key)
        self.canvas.bind("<Control-c>", self.on_ctrl_c)
        self.canvas.bind("<Control-x>", self.on_ctrl_x)
        self.canvas.bind("<Control-v>", self.on_ctrl_v)
        self.canvas.bind("<Control-V>", self.on_ctrl_shift_v)
        self.canvas.bind("<Control-a>", self.on_ctrl_a)
        self.canvas.bind("<Control-z>", self.on_ctrl_z)
        self.canvas.bind("<Control-y>", self.on_ctrl_y)
        self.canvas.bind("<Alt-F4>", self.exit)
        self.canvas.bind("<Control-s>", self.save)
        self.canvas.bind("<Control-o>", self.open)
        self.canvas.bind("<Home>", self.cursor_to_document_start)
        self.canvas.bind("<End>", self.cursor_to_document_end)

    def blink_cursor(self):
        self.cursor_visible = not self.cursor_visible
        self.draw_cursor()
        self.blinking_id = self.canvas.after(self.blinking_speed, self.blink_cursor)

    # Because you want to reset the cursor blink when the user types or moves the cursor
    def reset_cursor_blink(self):
        if hasattr(self, 'blinking_id'):
            self.canvas.after_cancel(self.blinking_id)
        self.cursor_visible = True
        self.blinking_id = self.canvas.after(self.blinking_speed, self.blink_cursor)
        self.draw_cursor()

    # End -1 means going to the end of the text
    def draw_lines(self, start: int = 0, end: int = -1):
        lines = self.model.get_lines()
        if end == -1 or end > len(lines):
            end = len(lines)

        # Delete
        for i in range(start, end):
            self.canvas.delete(f"line_{i}")

        # Delete any drawn lines that no longer exist
        index = len(lines)
        while self.canvas.find_withtag(f"line_{index}"):
            self.canvas.delete(f"line_{index}")
            index += 1
            self.draw_vertical_bar()

        # Draw
        y = self.y_offset + start * self.line_height
        for index, text in enumerate(self.model.lines_range_iter(start, end), start):
            self.canvas.create_text(self.x_offset, y, anchor=tk.NW, text=text, font=self.font, fill=self.text_color, tags=(f"line_{index}",))
            y += self.line_height
            if self.canvas.find_withtag("cursor"):
                self.canvas.tag_lower(f"line_{index}", "cursor")

        self.draw_vertical_bar()

    def draw_selections(self):
        self.canvas.delete("selection")
        selection_range = self.model.get_selection_range()
        if selection_range:
            start, end = selection_range.get_start(), selection_range.get_end()
            if start > end:
                start, end = end, start

            start_line, start_col = start.get_line(), start.get_column()
            end_line, end_col = end.get_line(), end.get_column()

            for line in range(start_line, end_line + 1):
                text = self.model.get_lines()[line]
                y = self.y_offset + line * self.line_height

                if line == start_line:
                    x_start = self.x_offset + self.font.measure(text[:start_col])
                else:
                    x_start = self.x_offset

                if line == end_line:
                    x_end = self.x_offset + self.font.measure(text[:end_col])
                else:
                    x_end = self.x_offset + self.font.measure(text)

                if x_start < x_end:
                    self.canvas.create_rectangle(
                        x_start, y,
                        x_end, y + self.line_height,
                        fill=self.selection_color,
                        outline="",
                        tags=("selection",)
                    )
            self.canvas.tag_lower("selection")

    def draw_cursor(self):
        self.canvas.delete("cursor")

        if self.cursor_visible:
            line = self.model.get_cursor_location().get_line()
            col = self.model.get_cursor_location().get_column()
            lines = self.model.get_lines()
            text_before_cursor = lines[line][:col] if line < len(lines) else ""
            cursor_x = self.x_offset + self.font.measure(text_before_cursor)    # Calculate the x position of the cursor based on font metrics
            cursor_y = self.y_offset + line * self.line_height
            self.canvas.create_line(cursor_x, cursor_y, cursor_x, cursor_y + self.line_height, fill=self.cursor_color, width=2, tags=("cursor",))

    # Draws a vertical bar at the left side of the text editor to indicate existing lines
    def draw_vertical_bar(self):
        self.canvas.delete("vertical_bar")

        height = self.y_offset * 2 + self.line_height * len(self.model.get_lines())
        self.canvas.create_line(2, 0, 2, height, fill=self.text_color, width=3, tags=("vertical_bar",))

    def redraw_all(self):
        self.draw_vertical_bar()
        self.draw_selections()
        self.draw_lines()
        self.draw_cursor()

    def update_cursor_location(self):
        self.reset_cursor_blink()
        self.draw_cursor()
        self.update_status_bar()

    def update_text(self, start_line: int, end_line: int):
        self.reset_cursor_blink()
        self.draw_lines(start_line, end_line)

    def update_selection(self, has_selection: bool):
        self.reset_cursor_blink()
        self.draw_selections()

    def on_left(self, event=None):
        ctrl = (event.state & self.CTRL_MASK) != 0
        shift = (event.state & self.SHIFT_MASK) != 0
        self.model.move_cursor_left(shift=shift, ctrl=ctrl)
        return "break"

    def on_right(self, event=None):
        ctrl = (event.state & self.CTRL_MASK) != 0
        shift = (event.state & self.SHIFT_MASK) != 0
        self.model.move_cursor_right(shift=shift, ctrl=ctrl)
        return "break"

    def on_up(self, event=None):
        shift = (event.state & self.SHIFT_MASK) != 0
        self.model.move_cursor_up(shift=shift)
        return "break"

    def on_down(self, event=None):
        shift = (event.state & self.SHIFT_MASK) != 0
        self.model.move_cursor_down(shift=shift)
        return "break"

    def on_backspace(self, event=None):
        ctrl = (event.state & self.CTRL_MASK) != 0
        text, location_range = self.model.delete_before(ctrl=ctrl)
        if text:
            self.undo_manager.push(DeleteAction(self.model, text, location_range))
        return "break"

    def on_delete(self, event=None):
        ctrl = (event.state & self.CTRL_MASK) != 0
        text, location_range = self.model.delete_after(ctrl=ctrl)
        if text:
            self.undo_manager.push(DeleteAction(self.model, text, location_range))
        return "break"
    
    def on_enter(self, event=None):
        self.undo_manager.push(InsertAction(self.model, *self.model.insert("\n")))
        return "break"

    def on_key(self, event=None):
        if event.char:
            self.undo_manager.push(InsertAction(self.model, *self.model.insert(event.char)))
        return "break"

    def on_ctrl_c(self, event=None):
        self.clipboard_stack.push(self.model.copy())
        return "break"

    def on_ctrl_x(self, event=None):
        text, location_range = self.model.cut()
        if text is not None:
            self.clipboard_stack.push(text)
            self.undo_manager.push(DeleteAction(self.model, text, location_range))
        return "break"

    def on_ctrl_v(self, event=None):
        text = self.clipboard_stack.peek()
        if text != "":
            self.undo_manager.push(InsertAction(self.model, *self.model.insert(text)))
        return "break"

    def on_ctrl_shift_v(self, event=None):
        text = self.clipboard_stack.peek()
        if text != "":
            self.undo_manager.push(InsertAction(self.model, *self.model.insert(text)))
            self.clipboard_stack.pop()
        return "break"

    def on_ctrl_a(self, event=None):
        self.model.select_all()
        return "break"
    
    def on_ctrl_z(self, event=None):
        self.undo_manager.undo()
        return "break"
    
    def on_ctrl_y(self, event=None):
        self.undo_manager.redo()
        return "break"
    
    def clear(self):
        self.undo_manager.push(DeleteAction(self.model, *self.model.clear()))

    def delete_selection(self):
        text, location_range = self.model.delete_range()
        if text:
            self.undo_manager.push(DeleteAction(self.model, text, location_range))

    def cursor_to_document_start(self, event=None):
        self.model.move_cursor_to_start()

    def cursor_to_document_end(self, event=None):
        self.model.move_cursor_to_end()

    def save(self, event=None):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write("\n".join(self.model.get_lines()))
                messagebox.showinfo("Save", "File saved successfully.")
            except Exception as e:
                messagebox.showerror("Save Error", f"An error occurred while saving the file: {e}")
        return "break"

    def open(self, event=None):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                self.model.clear()
                self.model.insert(content)
                messagebox.showinfo("Open", "File opened successfully.")
            except Exception as e:
                messagebox.showerror("Open Error", f"An error occurred while opening the file: {e}")
        return "break"

    def exit(self, event=None):
        if messagebox.askokcancel("Exit", "Do you really want to exit?"):
            self.set_visible(False)
            self.root.destroy()
        return "break"
    
    # For plugins
    def get_root(self) -> tk.Tk:
        return self.root
    def get_model(self) -> TextEditorModel:
        return self.model
    def get_clipboard_stack(self) -> ClipboardStack:
        return self.clipboard_stack
    def get_undo_manager(self) -> UndoManager:
        return self.undo_manager