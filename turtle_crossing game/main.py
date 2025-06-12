import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
scoreboard=Scoreboard()
car_manager=CarManager()

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkeypress(fun=player.up,key="Up")
    car_manager.create_car()
    car_manager.move()

    for car in car_manager.all_cars: # type: ignore
        if player.distance(car)<30: # type: ignore
            scoreboard.game_over()
            game_is_on=False
            screen.onkeypress(None, "Up")

    if player.ycor()==290: 
        player.up_level()
        scoreboard.up_level()
        car_manager.increment_speed()

screen.exitonclick()