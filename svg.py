from ShapeParser import Parser
from graphics import Graphics
import svgwrite  # requires python 3.6, pip install svgwrite


class SVG(Graphics):

    def create_graphics(self):
        return 'svg graphics'
