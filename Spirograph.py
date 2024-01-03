import turtle as t
import random


t.colormode(255)
timmy = t.Turtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r,g,b)


# make turtle draw a cicrle

def draw_spirograph(size_of_gap):
    angel = int(360 / size_of_gap)
    for _ in range( angel):
        
        timmy.speed("fastest")
        current_heading = timmy.heading()
        print(current_heading)
        timmy.setheading(current_heading + size_of_gap)
        color = random_color()
        timmy.pencolor(color)
        timmy.circle(100)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()