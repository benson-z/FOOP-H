import tkinter as tk
import tkinter.ttk as ttk
import turtle
import math

def pinwheel(size, sides):
    global pen
    pen.clear()
    pen.reset()
    pen.penup()
    pen.backward(size/6)
    pen.right(90)
    pen.forward(1/(math.tan(math.pi/sides))*size/6)
    pen.left(90)
    pen.pendown()
    for a in range(sides):
        pen.forward(size)
        pen.backward(2*size/3)
        pen.left(360/sides)
    pass

def asterisk(size, sides):
    global pen
    pen.clear()
    pen.reset()
    pen.left(90)
    for a in range(sides):
        pen.forward(size)
        pen.backward(size)
        pen.right(360/sides)

def polygon(size, sides):
    global pen
    pen.clear()
    pen.reset()
    pen.left(90)
    pen.penup()
    pen.forward(size)
    pen.left(90)
    pen.pendown()
    pen.back(math.tan(math.pi/sides)*size)
    for a in range(sides):
        pen.forward(math.tan(math.pi/sides)*size*2)
        pen.left(360/sides)

class Shapes(tk.Tk):
    selection = None
    canvas = None
    options = ["Polygon", "Polygon", "Asterisk", "Pinwheel"]
    size = None
    sides = None
    def __init__(self):
        super().__init__()
        self.geometry("600x740")
        self.resizable(False, False)

        self.canvas = tk.Canvas(self, width=600, height=600)
        self.canvas.pack()

        self.selection = tk.StringVar()
        self.size = tk.StringVar()
        self.sides = tk.StringVar()

        self.selection.set("Polygon")
        self.size.set("1")
        self.sides.set("3")

        ttk.OptionMenu(self, self.selection, *self.options).pack()
        ttk.Button(self, text="Draw", command=self.draw).pack()
        ttk.Entry(self, textvariable=self.size, validate="focusout", validatecommand=self.checkSize).pack()
        ttk.Entry(self, textvariable=self.sides, validate="focusout", validatecommand=self.checkSides).pack()
    def draw(self):
        shape = self.selection.get()
        if shape == "Polygon":
            polygon(int(self.size.get()), int(self.sides.get()))
        elif shape == "Asterisk":
            asterisk(int(self.size.get()), int(self.sides.get()))
        elif shape == "Pinwheel":
            pinwheel(int(self.size.get()), int(self.sides.get()))
    def getCanvas(self):
        return self.canvas
    def checkSize(self):
        return True
    def checkSides(self):
        return True

app = Shapes()
pen = turtle.RawTurtle(app.getCanvas())
pen.speed(0)
turtle.exitonclick()
app.mainloop()