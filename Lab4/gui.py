from __future__ import annotations
import tkinter as tk
from tkinter import simpledialog
from graphical_object import GraphicalObject
from document_model import DocumentModel
from drawing_canvas import DrawingCanvas
from state import State
from idle_state import IdleState
from add_shape_state import AddShapeState
from select_shape_state import SelectShapeState
from eraser_state import EraserState
from svg_renderer_impl import SVGRendererImpl
from collections import deque
from line_segment import LineSegment
from oval import Oval
from composite_shape import CompositeShape

class GUI:
    def __init__(self, objects: list[GraphicalObject]):
        self.objects: list[GraphicalObject] = objects
        self.visible: bool = False

        self.canvas_width: int = 1600
        self.canvas_height: int = 900

        self.root: tk.Tk = tk.Tk()
        self.root.title("SVG Editor")

        self.document_model: DocumentModel = DocumentModel()

        self.toolbar: tk.Frame = tk.Frame(self.root)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.canvas: DrawingCanvas = DrawingCanvas(self.root, self, self.document_model, self.canvas_width, self.canvas_height)
        self.canvas.pack()

        self.state: State = IdleState()

        self.buttons: dict[str, tk.Button] = {}

        export_svg_button = tk.Button(self.toolbar, text="Export SVG", command=lambda: self.export_svg())
        export_svg_button.pack(side=tk.LEFT, padx=2, pady=2)
        self.buttons['export_svg'] = export_svg_button

        save_button = tk.Button(self.toolbar, text="Save", command=lambda: self.save())
        save_button.pack(side=tk.LEFT, padx=2, pady=2)
        self.buttons['save'] = save_button

        load_button = tk.Button(self.toolbar, text="Load", command=lambda: self.load())
        load_button.pack(side=tk.LEFT, padx=2, pady=2)
        self.buttons['load'] = load_button

        select_btn = tk.Button(self.toolbar, text="Select", command=lambda: self.set_state(SelectShapeState(self.document_model), 'select'))
        select_btn.pack(side=tk.LEFT, padx=2, pady=2)
        self.buttons['select'] = select_btn

        eraser_btn = tk.Button(self.toolbar, text="Eraser", command=lambda: self.set_state(EraserState(self.document_model), 'eraser'))
        eraser_btn.pack(side=tk.LEFT, padx=2, pady=2)
        self.buttons['eraser'] = eraser_btn

        for obj in self.objects:
            btn = tk.Button(self.toolbar, text=f"{obj.get_shape_name()}", command=lambda o=obj: self.set_state_add_shape(o))
            btn.pack(side=tk.LEFT, padx=2, pady=2)
            self.buttons[obj.get_shape_name()] = btn


        self.active_button: str = None

    def set_visible(self, visible: bool):
        self.visible = visible
        if visible:
            self.root.mainloop()

    def get_state(self) -> State:
        return self.state

    def set_state(self, state: State, new_active_button: str = None):
        self.state.on_leaving()
        self.state = state
        if self.active_button:
            self.buttons[self.active_button].config(bg="white")
        if new_active_button:
            self.buttons[new_active_button].config(bg="yellow")
        self.active_button = new_active_button

    def set_state_add_shape(self, prototype: GraphicalObject):
        state = AddShapeState(self.document_model, prototype)
        self.set_state(state, prototype.get_shape_name())

    def export_svg(self):
        file_name = tk.simpledialog.askstring("Export SVG", "Enter file name:")
        if not file_name:
            return
        renderer = SVGRendererImpl(file_name, self.canvas_width, self.canvas_height)
        for obj in self.document_model.get_list():
            obj.render(renderer, self.document_model, False)
        renderer.close()

    def save(self):
        file_name = tk.simpledialog.askstring("Save", "Enter file name:")
        if not file_name:
            return
        
        rows = []
        for obj in self.document_model.get_list():
            obj.save(rows)
        with open(file_name, 'w') as file:
            file.write('\n'.join(rows))

    def load(self):
        file_name = tk.simpledialog.askstring("Load", "Enter file name:")
        if not file_name:
            return
        try:        
            prototypes = {
                "@LINE": LineSegment,
                "@OVAL": Oval,
                "@COMP": CompositeShape
            }

            stack: deque[GraphicalObject] = deque()

            with open(file_name, 'r') as file:
                self.document_model.clear()
                
                for line in file:
                    parts = line.strip().split()
                    shape_id = parts[0]
                    if shape_id in prototypes:
                        prototypes[shape_id].load(stack, ' '.join(parts[1:]))
                    else:
                        raise ValueError(f"Unknown shape ID: {shape_id}")
            
            while stack:
                obj = stack.popleft()
                self.document_model.add_graphical_object(obj)

        except FileNotFoundError:
            tk.messagebox.showerror("Error", f"File {file_name} not found.")