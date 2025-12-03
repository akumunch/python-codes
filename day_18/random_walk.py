# import turtle as t
# import random

# tim = t.Turtle()
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]

# tim.pensize(15)
# tim.speed("fastest")

# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# t.done()



fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
try:    
    def make_pie(index):
        fruit = fruits[index]
        print(fruit + " pie")
    make_pie(4) 
except IndexError: 
    print("Fruit pie")

