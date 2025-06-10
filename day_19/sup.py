from turtle import Turtle, Screen
import turtle 

tim= Turtle()
screen=Screen()
initial_position=tim.pos()
tim.shape("turtle")
tim.color("cyan","black")
turtle.bgcolor("brown")

def backwards():
    tim.backward(10)

def forwards():
    tim.forward(10)

def left(): 
   setheading=tim.heading()+10
   tim.setheading(setheading)

def right():
    setheading=tim.heading()-10
    tim.setheading(setheading)

def bye():
    turtle.bye()

def clear():
    tim.goto(initial_position)
    tim.clear()


screen.listen()
screen.onkeypress(key="W",fun=forwards)
screen.onkeypress(key="A",fun=left)
screen.onkeypress(key="S",fun=backwards)
screen.onclick(tim.goto) # Subsequently clicking into the TurtleScreen will
screen.onkeypress(key="D",fun=right)
screen.onkey(key="b",fun=bye)
screen.onkey(key="B",fun=bye)
screen.onkey(key='C',fun=clear)
turtle.mainloop()