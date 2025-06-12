from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars=[]
        self.move_distance=STARTING_MOVE_DISTANCE
    def create_car(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_car=Turtle(shape="square")
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            GO_X=300
            go_y=random.randint(-250,250)
            new_car.goto(GO_X,go_y)
            self.all_cars.append(new_car) # type: ignore
    def move(self):
        for car in self.all_cars: # type: ignore
            car.backward(STARTING_MOVE_DISTANCE) # type: ignore
    def increment_speed(self):
        self.move_distance+=MOVE_INCREMENT