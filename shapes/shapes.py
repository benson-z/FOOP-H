import tkinter as tk
import tkinter.ttk as ttk
import turtle

def pinwheel(size, sides):
    global pen
    print("Pinwheel")
    pass

def polygon(size, sides):
    global pen
    print("Polygon")
    pass

def asterisk(size, sides):
    global pen
    print("Asterisk")
    pass

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
        ttk.Entry(self, textvariable=self.size).pack()
        ttk.Entry(self, textvariable=self.sides).pack()
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
    def checkNum(self):
        return True

app = Shapes()
pen = turtle.RawTurtle(app.getCanvas())
turtle.exitonclick()
app.mainloop()