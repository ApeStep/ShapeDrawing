from abc import ABC, abstractmethod
from graphics import Graphics

# ABSTRACTION
# Used by the client


class Shape(ABC):
    def __init__(self, Graphics: Graphics):
        self.Graphics = Graphics

    @abstractmethod
    def draw(self):
        pass
