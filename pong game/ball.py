from turtle import Turtle
DEFAULT=10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_move=DEFAULT
        self.y_move=DEFAULT
        self.move_speed=0.1
    
    def move(self):
        x_cor=self.xcor()+self.x_move
        y_cor=self.ycor()+self.y_move
        self.goto(x_cor,y_cor)
    
    def bounce_y(self):
        self.y_move*=-1
    
    def bounce_x(self):
        self.x_move*=-1
        self.move_speed*=0.9
    
    def reset_position(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_x()
