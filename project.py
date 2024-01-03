import colorgram
import turtle as t
import random

t.colormode(255)

colors = colorgram.extract("hirst_art.jpg", 20)

rgb_colors = [ color.rgb for color in colors ]

timmy = t.Turtle()
timmy.penup()
timmy.hideturtle()

def draw_dot():
    timmy.dot(20, random.choice(rgb_colors))
    timmy.forward(50)

timmy.speed('fastest')

for i in range(1, 10):
    for _ in range(1, 10):
        draw_dot()
    
    current_pos = timmy.pos()
    

    timmy.goto(0.0, current_pos[1] + 50)
    
    




screen = t.Screen()
screen.exitonclick()