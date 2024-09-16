from turtle import Turtle


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-400, -300)
        self.pendown()
        self.speed("fastest")
        self.width(10)
        self.color("white")
        for _ in range(2):
            self.forward(800)
            self.left(90)
            self.fd(600)
            self.left(90)

    @staticmethod
    def center_line():
        joe = Turtle()
        joe.hideturtle()
        joe.penup()
        joe.goto(0, -285)
        joe.setheading(90)
        for i in range(10):
            joe.color("white")
            joe.pendown()
            joe.fd(30)
            joe.penup()
            joe.fd(30)

    @staticmethod
    def game_over():
        joe = Turtle()
        joe.hideturtle()
        joe.penup()
        joe.color("red")
        joe.write("End game", move=False, align='center', font=('Arial', 20, 'normal'))
