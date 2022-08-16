# see turtle functions at https://docs.python.org/3/library/turtle.html

import turtle
import random
import time;

#makes a rectangle of specified length/width
#can also draw squares ; )
def rectangle(length, width):
  for x in range(2):
    tia.forward(length)
    tia.right(90)
    tia.forward(width)
    tia.right(90)



    
#creating a drawing - don't alter ; )
tia = turtle.Turtle()
    
#change the colors of your drawings
turtle.colormode(255)
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
tia.pencolor(r, g, b)

#making some variables - use or delete
tia.speed(0)
degree = 10
radius = 50


#making a drawing with the shapes I want
tia.circle(radius)
tia.right(degree) 
rectangle(20, 40)

tia.penup()
tia.goto(150, 150)
tia.pendown()

tia.goto(150,100)
tia.goto(180,120)
tia.goto(150,150)#making a triangle

turtle.Screen().exitonclick()