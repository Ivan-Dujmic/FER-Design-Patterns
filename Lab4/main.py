from __future__ import annotations
from graphical_object import GraphicalObject
from point import Point
from line_segment import LineSegment
from oval import Oval
from gui import GUI

def main():
    objects: list[GraphicalObject] = []

    objects.append(LineSegment(Point(0, 0), Point(50, 50)))
    objects.append(Oval(Point(50, 0), Point(0, 25)))

    gui = GUI(objects)
    gui.set_visible(True)

if __name__ == "__main__":
    main()