from shape import Shape
from tkinter import Canvas
from graphics import Graphics

# REFINED ABSTRACTION CIRCLE


class Circle(Shape):

    def __init__(self, x: int, y: int, radius: int):
        self.x: int = x
        self.y: int = y
        self.radius: int = radius
        super().__init__()

    def draw(self):
        self.Graphics.create_graphics()
