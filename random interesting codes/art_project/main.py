from turtle import Turtle, Screen
import turtle,colorgram
import colors,random
import re

colours=colors.turtle_colors

turtle.colormode(255)
tim = Turtle()
fill_color=random.choice(colours)
screen= Screen()
screen.screensize(2000000,15000000,"aquamarine")
tim.speed(10)

tim.setheading(0)

def tim_makeshapes():
    for i in range(8):
        pen_color=random.choice(colours)
        tim.color(pen_color, fill_color)
        for j in range(i+3):
            tim.forward(100)
            tim.right(360/(i+3))
def tim_makesquare():
    for i in range(1,5):
        tim.forward(100)
        tim.lt(90)
def tim_makedashedline():
    for i in range (1,5):
        tim.pendown()
        tim.forward(10)
        tim.penup()
        tim.forward(10)

def colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    t=(r,g,b)
    return t
def tim_randomwalk():
    #thickness of line, speed, maintain random color, out of four directions choose a random direction and walk 100 spaces forward. 
    tim.pensize(10)
    num=random.randint(1,250)
    walk_num= random.randrange(1,num)
    def direction():
        directions = [0, 90, 180, 270]
        tim.setheading(random.choice(directions))
    for i in range(walk_num):
        tim.color(colour())
        direction()
        tim.forward(30)
    
def tim_makespirograph():
    for i in range(1,72):
        tim.color(colour())
        tim.circle(100)
        tim.left(5)

rgb_colors=[(133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209)]

# colors=colorgram.extract('dot_painting.jpg',30)
# for color in colors: 
    # r=color.rgb.r
    # g=color.rgb.g
    # b=color.rgb.b
    # rgb_colors.append((r,g,b))

#10 by 10, 20 dot size, 50 paces gap. 

def dots():
    tim.pendown()
    tim.speed(100)
    color_=random.choice(rgb_colors)
    tim.dot(20,color_)
    tim.penup()
    tim.forward(50)
    tim.pendown()

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
for i in range(10):
    for j in range(10):
        dots()
    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.setheading(0)
    tim.pendown()
screen.exitonclick()
