from tkinter import *


#def add(*args):
#     sum=0
#     for n in args: 
#         sum+=n
#     return sum

# sum_val= add(5,4,5,8)
# print(sum_val)


window= Tk()
window.title("hello world!")
window.minsize(width=370,height=300)
window.config(padx=20,pady=20)

fred= Label(text="This is a Label",font=("Arial",24))
fred.grid(row=0,column=0)

input= Entry(width=15)
input.grid(row=2,column=3)

def do_this():
    print("Button clicked")
    fred.config(text=input.get())

button= Button(text= "Click me_1", command= do_this)
button.grid(row=1,column=1)

new_button= Button(text= "Click me_2", command= do_this)
new_button.grid(row=0,column=2)


window.mainloop()

