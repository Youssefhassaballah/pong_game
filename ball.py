from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(45)
        self.move()

    def move(self):
        self.fd(10)

    def collision_wall(self):
        h = self.heading()
        if self.ycor() > 285:
            self.setheading(360-h)
        elif self.ycor() < -285:
            self.setheading(180-(h-180))
