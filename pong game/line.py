from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0,280)
        self.setheading(270)
        for _ in range(28):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)