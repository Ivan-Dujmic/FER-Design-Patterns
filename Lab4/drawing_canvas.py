from __future__ import annotations
from typing import TYPE_CHECKING
import tkinter as tk
from document_model import DocumentModel
from document_model_listener import DocumentModelListener
from g2d_renderer import G2DRenderer
from graphical_object import GraphicalObject
from point import Point
from state import State
from idle_state import IdleState

if TYPE_CHECKING:
    from gui import GUI

class DrawingCanvas(tk.Frame, DocumentModelListener):
    SHIFT_MASK = 0x0001
    CTRL_MASK = 0x0004

    def __init__(self, master: tk.Tk, gui: GUI, document_model: DocumentModel, width: int, height: int):
        super().__init__(master)
        self.master: tk.Tk = master
        self.gui: GUI = gui
        self.document_model: DocumentModel = document_model
        self.canvas: tk.Canvas = tk.Canvas(master, bg='white', width=width, height=height)
        self.canvas.pack()

        self.document_model.add_document_model_listener(self)

        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<ButtonRelease-1>", self.on_click_release)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<Key>", self.on_key_press)
        self.canvas.bind("<Escape>", self.on_escape)

        self.canvas.focus_set()

    def document_change(self):
        self.redraw()
        pass

    def get_renderer(self) -> G2DRenderer:
        return G2DRenderer(self.canvas)

    def paint_component(self):
        renderer = self.get_renderer()
        for obj in self.document_model.get_list():
            obj.render(renderer, self.document_model, True)
            self.gui.get_state().after_draw(renderer, obj)
        self.gui.get_state().after_draw(renderer, None)

    def redraw(self):
        self.canvas.delete("all")
        self.paint_component()

    def on_click(self, event: tk.Event):
        self.gui.get_state().mouse_down(Point(event.x, event.y), event.state & self.SHIFT_MASK, event.state & self.CTRL_MASK)

        return 'break'

    def on_click_release(self, event: tk.Event):
        self.gui.get_state().mouse_up(Point(event.x, event.y), event.state & self.SHIFT_MASK, event.state & self.CTRL_MASK)

        return 'break'

    def on_drag(self, event: tk.Event):
        self.gui.get_state().mouse_dragged(Point(event.x, event.y))

        return 'break'

    def on_key_press(self, event: tk.Event):
        self.gui.get_state().key_pressed(event.keycode)

        return 'break'

    def on_escape(self, event: tk.Event):
        self.gui.set_state(IdleState(), None)

        return 'break'