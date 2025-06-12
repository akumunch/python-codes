from turtle import Turtle
import winsound
import os

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=-1
        self.hideturtle()
        self.penup()
        self.goto(-200,260)
        self.up_level()
    def up_level(self):
        self.level+=1
        self.clear()
        self.write(f"Level: {self.level}",align="left",font=FONT)
    def game_over(self):
        sound_path = os.path.join(os.path.dirname(__file__), "game_over.wav")
        print(f"Playing: {sound_path}")
        winsound.PlaySound(sound_path, winsound.SND_ASYNC)
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)
        
