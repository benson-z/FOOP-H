import tkinter as tk
import turtle
import tkinter.ttk as ttk

screen = turtle.Screen()
pen = turtle.RawTurtle(screen)

def pinwheel(size, shape):
    pass

def polygon(size, shape):
    pass

def asterisk(size, shape):
    pass

class Selector(tk.Frame):
    def __init__(self):
        super().__init__()
    def update(self):
        pass #draws the selected shape

canvas = screen.getcanvas()
frame = Selector(canvas.master)
canvas.create_window(0, 500, window=frame)
turtle.Screen().exitonclick()