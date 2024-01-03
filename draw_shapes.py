from turtle import Turtle, Screen

CIRCLE = 360

shapes = [(3, "blue"), 
          (4, "dark green"), 
          (5, "light salmon"), 
          (6,"saddle brown"), 
          (7, "medium slate blue" ), 
          (8,"light slate gray"),
          (9, "tomato"),
          (10, "dark blue")
          ]


timmy_turle = Turtle()

timmy_turle.shape("turtle")

def draw_shape(shape):
    angle = CIRCLE / shape[0]

    for _ in range(shape[0]):
        timmy_turle.color(shape[1])
        timmy_turle.forward(100)
        angle = CIRCLE / shape[0]
        timmy_turle.right(angle)


#  Loop through all the different shapes
for shape in shapes:
    draw_shape(shape)
        
    

# for _ in range(4):
#     timmy_turle.forward(100)
#     timmy_turle.right(90)

# for _ in range(15):
#     timmy_turle.pendown()
#     timmy_turle.forward(10)
#     timmy_turle.penup()
#     timmy_turle.forward(10)



screen = Screen()
screen.exitonclick()

