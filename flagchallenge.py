# Benson Zhou - Turtle Create a Flag Challenge

import turtle;
import math;

pen = turtle.Turtle()

pen.speed(0)

#draws a line
def drawLine(angle, length):
	turtle.pendown()
	turtle.setheading(angle)
	turtle.forward(length)

#makes a star with a specified size
def star(x, y, size = 1, color = "#ffffff"):
	pen.penup()
	pen.goto(x, y)
	pen.pendown()
	pen.color(color)
	pen.begin_fill()
	pen.setheading(0)
	for z in range(5):
		pen.forward(size)
		pen.left(72)
		pen.forward(size)
		pen.right(144)
	pen.end_fill()

# Draw a rectangle
def rectangle(x, y, length, width):
	pen.penup()
	pen.setheading(0)
	pen.goto(x, y)
	pen.pendown()
	for x in range(2):
		pen.forward(length)
		pen.right(90)
		pen.forward(width)
		pen.right(90)

#Draw a rectangle with fill
def rectangleFill(x, y, length, width, color = "#ffffff"):
	pen.penup()
	pen.setheading(0)
	pen.color(color)
	pen.goto(x, y)
	pen.pendown()
	pen.begin_fill()
	for x in range(2):
 		pen.forward(length)
 		pen.right(90)
 		pen.forward(width)
 		pen.right(90)
	pen.end_fill()

# Flag border
rectangle(-248, 131, 496, 262)

# Red and White stripes (494 by 260)
for stripe in range (13):
	if stripe % 2 == 0:
		color = "#B22234"
	else:
		color = "#ffffff"
	rectangleFill(-247, 130 - stripe * 20, 494, 20, color)

# Blue Rectangle
rectangleFill(-247, 130, 198, 140, "#3C3B6E")

# Stars
for row in range(1, 10):
	for column in range(5 + row%2):
		star(-220 - row%2*16.5 + 33*column, - 7 + 14*row, 4)

# Move turtle out of the way
pen.penup()
pen.goto(-500,-500)

# Keep the window open
turtle.Screen().exitonclick()