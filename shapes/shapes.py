import tkinter as tk
import tkinter.ttk as ttk
import turtle
import math

# Draw pinwheel
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

# Draw Asterisk
def asterisk(size, sides):
    global pen
    pen.clear()
    pen.reset()
    pen.left(90)
    for a in range(sides):
        pen.forward(size)
        pen.backward(size)
        pen.right(360/sides)

# Draw Polycon
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

# Main Tk Window
class Shapes(tk.Tk):
    # Initialize variables
    selection = None
    canvas = None
    options = ["Polygon", "Polygon", "Asterisk", "Pinwheel"]
    size = None
    sides = None
    width = None
    frame1 = None
    drawButton = None
    # Window Layout
    def __init__(self):
        super().__init__()
        self.geometry("740x600")
        self.title("Draw Shapes")
        self.resizable(False, False)
        
        frame1 = tk.Frame(self)

        self.canvas = tk.Canvas(self, width=600, height=600)
        self.canvas.pack(side=tk.LEFT)

        self.selection = tk.StringVar()
        self.size = tk.StringVar()
        self.sides = tk.StringVar()
        self.width = tk.StringVar()

        self.selection.set("Polygon")
        self.size.set("100")
        self.sides.set("3")
        self.width.set("1")

        frame1.pack()
        ttk.Label(frame1, text="Options", font=("", 20)).pack(pady=20)
        ttk.Label(frame1, text="Shape").pack()
        ttk.OptionMenu(frame1, self.selection, *self.options).pack()
        ttk.Label(frame1, text="Shape Size").pack(pady=(15, 0))
        ttk.Entry(frame1, textvariable=self.size, validate="focusout", validatecommand=self.checkSize).pack(padx=20)
        ttk.Label(frame1, text="Shape Sides").pack(pady=(5, 0))
        ttk.Entry(frame1, textvariable=self.sides, validate="focusout", validatecommand=self.checkSides).pack(padx=20)
        self.drawButton = ttk.Button(frame1, text="Draw", command=self.draw)
        self.drawButton.pack(pady=(330, 0))
    # Select Draw Function
    def draw(self):
        self.drawButton.config(state = tk.DISABLED)
        pen.width(int(self.width.get()))
        shape = self.selection.get()
        if shape == "Polygon":
            polygon(int(self.size.get()), int(self.sides.get()))
        elif shape == "Asterisk":
            asterisk(int(self.size.get()), int(self.sides.get()))
        elif shape == "Pinwheel":
            pinwheel(int(self.size.get()), int(self.sides.get()))
        self.drawButton.config(state = tk.NORMAL)
    # Returns the Tkinter canvas for initializing turtle
    def getCanvas(self):
        return self.canvas
    # Validate size is an allowed value
    def checkSize(self):
        try:
            if int(self.size.get()) > 0:
                return True
            raise Exception("Has to be a positive number")
        except:
            self.size.set("100")
            return False
    # Validate sides is an allowed value
    def checkSides(self):
        try:
            if int(self.size.get()) > 0:
                return True
            raise Exception("Has to be a positive number")
        except:
            self.sides.set("3")
            return False

app = Shapes()
# Initialize a turtle instance to the tkinter canvas
pen = turtle.RawTurtle(app.getCanvas())
pen.speed(0)
turtle.done()
app.mainloop()