from graphics import Graphics
from tkinter import Canvas
from ShapeParser import Parser
from star import Star
from circle import Circle
from rectangle import Rectangle
# from typing import List
# from shape import Shape

# CONCRETE IMPLEMENTATION FOR DRAWING SHAPEN ON THE CANVAS OF THE GUI


class CanvasGraphics(Graphics):

    def create_graphics(self):
        return 'kanker zooi'

        # def draw_circle(self, canvas: Canvas):
        #     self.circle = Circle()
        #     self.canvas.create_oval(self.circle.x - self.circle.radius, self.circle.y - self.circle.radius,
        #                             self.circle.x + self.circle.radius, self.circle.y + self.circle.radius)

        # def draw_rectangle(self, canvas: Canvas):
        #     self.rectangle = Rectangle()
        #     self._create_line(self.rectangle.x, self.rectangle.y,
        #                       self.rectangle.x + self.rectangle.width, self.rectangle.y,
        #                       self.rectangle.x + self.rectangle.width, self.rectangle.y + self.rectangle.height,
        #                       self.rectangle.x, self.rectangle.y + self.rectangle.height,
        #                       self.rectangle.x, self.rectangle.y)

        # def draw_star(self, canvas: Canvas):
        #     self.star = Star()

        #     numPoints = 5
        #     pts = []
        #     rx = self.star.width / 2
        #     ry = self.star.height / 2
        #     cx = self.star.x + rx
        #     cy = self.star.y + ry
        #     theta = -math.pi / 2
        #     dtheta = 4 * math.pi / numPoints

        #     for i in range(0, numPoints + 1):
        #         pts.append(
        #             int(round(cx + rx * math.cos(theta))))
        #         pts.append(
        #             int(round(cy + ry * math.sin(theta)))
        #         )
        #         theta += dtheta

        #     # we use the '*' syntax here to convert the list of points to function arguments
        #     canvas.create_line(*pts)

        # if shape == Circle:
        #     draw_circle(self.canvas)
        # elif shape == Rectangle:
        #     draw_rectangle(self.canvas)
        # else:
        #     draw_star(self.canvas)
