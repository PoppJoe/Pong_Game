from turtle import Turtle
MOVING_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.goto(position)


    def move_up(self):
        new_y_pos = self.ycor() + MOVING_DISTANCE
        self.goto(self.xcor(), new_y_pos)

    def move_down(self):
        new_y_pos = self.ycor() - MOVING_DISTANCE
        self.goto(self.xcor(), new_y_pos)
