import turtle
import random

pen = turtle.Screen()
pen.bgpic("../resources/0008563307099_1_A1C1_0600.png")
choices = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', "Don't count on it", 'my reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

def answer(x, y):
    turtle.reset()
    turtle.penup()
    turtle.right(90)
    turtle.forward(200)
    turtle.color(1, 0, 1)
    turtle.textinput("Input", "Ask a question")
    turtle.write(random.choice(choices), move=False, align="center", font=("Arial", 40, "normal"))

turtle.onscreenclick(answer)
turtle.mainloop()