from shape import Shape
from tkinter import Canvas
from graphics import Graphics

# REFINED ABSTRACTION RECTANGLE


class Rectangle(Shape):

    def __init__(self, x: int, y: int, width: int, height: int):
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
        super().__init__()

    def draw(self):
        self.Graphics.create_graphics()
