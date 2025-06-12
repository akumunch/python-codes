import os
import winsound
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10

class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.penup()
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.fd(MOVE_DISTANCE)
        sound_path = os.path.join(os.path.dirname(__file__), "bounce.wav")
        print(f"Playing: {sound_path}")
        winsound.PlaySound(sound_path, winsound.SND_ASYNC)
            

    def up_level(self):
        self.goto(STARTING_POSITION)
