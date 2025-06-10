from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
# from something import definition

# defin=definition()

screen=Screen()
screen.setup(width=600,height=600)
screen.title("Snake game")
screen.bgcolor("black")
screen.tracer(0)
snake=Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
food=Food()
scoreboard=Scoreboard()

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increment()
    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        scoreboard.game_over()
        game_is_on = False
    
    for seg in snake.segments[1:]:
        if snake.head.distance(seg)<10:
            game_is_on=False
            scoreboard.game_over()

screen.exitonclick()
