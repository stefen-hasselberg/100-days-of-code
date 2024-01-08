from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forward():
  timmy.forward(10)

def move_back():
  timmy.back(10)

def turn_left():
  timmy.left(10)

def turn_right():
  timmy.right(10)

def clear_drawing():
  timmy.reset()

screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_back)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="c", fun=clear_drawing)

screen.exitonclick()