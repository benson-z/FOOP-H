# Benson Zhou - Turtle Create a Flag Challenge

import turtle;

#Create turtle
pen = turtle.Turtle()

# Set turtle speed to fastest
pen.speed(0)

# Draw a star
def star(x, y, size = 1, color = "#ffffff", rotation = 0):
	pen.penup()
	pen.goto(x, y)
	pen.pendown()
	pen.color(color)
	pen.begin_fill()
	pen.setheading(rotation)
	for z in range(5):
		pen.forward(size)
		pen.left(72)
		pen.forward(size)
		pen.right(144)
	pen.end_fill()

# Draw a rectangle
def rectangle(x, y, length, width, color = "#ffffff", fill = False):
	pen.penup()
	pen.setheading(0)
	pen.color(color)
	pen.goto(x, y)
	pen.pendown()
	if fill:
		pen.begin_fill()
	for x in range(2):
		pen.forward(length)
		pen.right(90)
		pen.forward(width)
		pen.right(90)
	if fill:
		pen.end_fill()

# Flag border
rectangle(-248, 131, 496, 262, "#000000")

# Red and White stripes (494 pixels by 260 pixels)
for stripe in range (13):
	if stripe % 2 == 0:
		color = "#B22234"
	else:
		color = "#ffffff"
	rectangle(-247, 130 - stripe * 20, 494, 20, color, True)

# Blue Rectangle
rectangle(-247, 130, 198, 139, "#3C3B6E", True)

# Stars
for row in range(1, 10):
	for column in range(5 + row%2):
		star(-220 - row%2*16.5 + 33*column, - 7 + 14*row, 4)

# Move turtle out of the way
pen.penup()
pen.goto(-500,-500)

# Keep the window open
turtle.Screen().exitonclick()