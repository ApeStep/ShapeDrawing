from tkinter import Tk, Canvas, Frame, Menu, BOTH, filedialog
from rectangle import Rectangle
from circle import Circle
from shape import Shape
from star import Star
from ShapeParser import Parser
from svg import SVG
from canvas import CanvasGraphics

# CLIENT


class ShapeDrawing(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.widgets()
        self.shapes = []

    def widgets(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        fileMenu.add_command(label="Clear", command=self.onClear)
        fileMenu.add_command(label="Export", command=self.onExport)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)

        self.master.title("Shape Drawing")
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self)
        self.canvas.pack(fill=BOTH, expand=1)

    def onOpen(self):
        # OPEN JSON FILE WITH SHAPE PROPERTIES
        file = filedialog.askopenfilename(title="Select file")
        if not file:
            return

        # RETURNS [Circle(x,y,r),Rectangle(x,y,w,h),Star(x,y,w,h)
        parser = Parser()
        self.shapes = parser.parse_shapes(file)

        # DELETES ANY EXISTING SHAPES BEFORE DRAWING SHAPES
        self.canvas.delete("all")

        canvas_graphics = CanvasGraphics()

        for shape in self.shapes:
            Shape(shape, canvas_graphics.create_graphics(shape))

    def onClear(self):
        self.canvas.delete("all")
        self.shapes = []

    def onExport(self):
        # needs implementation of svg graphics

        file = filedialog.asksaveasfile(title="Enter file name")

        parser = Parser()
        self.shapes = parser.parse_shapes(self.file)

        for shape in self.shapes:
            Shape(shape, create_graphics(shape))

    def onExit(self):
        self.quit()


def main():

    root = Tk()
    root.title("Shape Drawing")
    root.geometry("400x250+300+300")
    app = ShapeDrawing(root)

    root.mainloop()


if __name__ == '__main__':
    main()
