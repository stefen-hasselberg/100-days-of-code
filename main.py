from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange","yellow", "green", "blue", "purple"]



turtles = []

for turtle in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle])
    y_pos = turtle * 40
    new_turtle.goto(x= -230, y = -70 + y_pos)
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You won, the winning color was {turtle.pencolor()}")
            else:
                print(f"You lost, the winning color was {turtle.pencolor()}")
            
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

        
            

    

screen.exitonclick()