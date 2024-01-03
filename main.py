import turtle as t
import random


timmy = t.Turtle()
t.colormode(255)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0, 90,  180, 270 ]

rgb_range = range(0, 256)

steps = range(0, 50)
angles = range(0, 361)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r,g,b)

for _ in range(0, 200):
    color = (random_color())
  
    timmy.pensize(10)
    timmy.speed("fastest")

    angle = random.choice(direction)

    timmy.pencolor(color)
    timmy.forward(30)
    timmy.setheading(angle)
    


screen = t.Screen()
screen.exitonclick()