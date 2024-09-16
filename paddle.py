from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(x, 0)

    def move_up(self):
        if not (self.ycor() >= 240):
            self.forward(20)

    def move_down(self):
        if not (self.ycor() <= -240):
            self.back(20)
