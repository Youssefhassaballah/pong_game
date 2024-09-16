from turtle import Turtle
font = ('Courier', 35, 'normal')
align = 'center'


class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.score = 0

    def the_score(self):
        self.clear()
        self.write(f"{self.score}", False, align, font)
