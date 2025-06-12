from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from line import Line
import time

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
line=Line()

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")


game_is_on=True
while game_is_on:
    
    if scoreboard.l_score>=5:
        scoreboard.winner(side=1)
        game_is_on=False
    if scoreboard.r_score>=5:
        scoreboard.winner(side=2)
        game_is_on=False
    
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    if abs(ball.ycor())>280:
        ball.bounce_y()
    
    #ball hit paddle
    if (ball.distance(r_paddle)<50 and ball.xcor()>320 and ball.x_move>0) or (ball.distance(l_paddle)<50 and ball.xcor()<-320 and ball.x_move<0):
        ball.bounce_x()
    
    if ball.xcor()>380:
        scoreboard.l_point()
        ball.reset_position()
    
    if ball.xcor()<-380:
        scoreboard.r_point()
        ball.reset_position()


screen.exitonclick()