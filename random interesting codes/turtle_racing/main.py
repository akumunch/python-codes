from turtle import Turtle, Screen
import random

is_bet=False
screen=Screen()
screen.setup(width=500, height=400)
user_bet= screen.textinput(title="Make your bet",prompt="Which turtle will win the race?" \
"Enter a color: ")
colors= ["red","orange","yellow","green","blue","purple"]
turtles=[]
for i in range(6): #0,1,2,3,4,5
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(-220,150-(50*(i-1)))

if user_bet: 
    is_bet=True

while is_bet: 
    for turtle in turtles :
        if turtle.xcor()>220:
            is_bet=False
            winning_turtle_color=turtle.pencolor()
            if winning_turtle_color==user_bet: 
                print(f"Your bet was correct, {winning_turtle_color} won the race.")
            else: 
                print(f"Your bet was wrong, {winning_turtle_color} won the race.")
        fw_value=random.randint(0,10)
        turtle.forward(fw_value)

#tim,tom,jam,kam,lam,sam

screen.exitonclick()