from abc import ABC, abstractmethod
from tkinter import Canvas
from graphics import Graphics

# ABSTRACTION
# Used by the client


class Shape(ABC):
    def __init__(self, Graphics):
        self.Graphics = Graphics

    @abstractmethod
    def draw(self):
        pass
