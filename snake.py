from turtle import Turtle


MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for i in range(0,3):
            segment = Turtle(shape="square")
            segment.penup()
            segment.color("white")
            x_pos = i * 20
            segment.goto(x= 0 - x_pos, y = 0 )
            self.segments.append(segment)


    def move(self):
        for seq_num in range(len(self.segments) -1,  0 , -1):
            new_pos = self.segments[seq_num - 1].pos()
            self.segments[seq_num].setpos(new_pos) 

        self.head.forward(MOVE_DISTANCE)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
