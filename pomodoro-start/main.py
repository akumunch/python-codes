from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
ticks=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global ticks
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    ticks=0
    tick_label.config(text="")
    canvas.itemconfig(time_text,text="00:00")
    global reps 
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    work_sec=WORK_MIN*60
    
    if(reps%2==1):
        timer_label.config(text="Work")
        count_down(work_sec)    
    
    elif(reps%8==0):
        timer_label.config(text="20 Mins Break",fg=RED)
        count_down(long_break_sec)

    else: 
        timer_label.config(text="5 Mins Break",fg=PINK)
        count_down(short_break_sec)     
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    global ticks
    count_min=count//60
    count_sec=count%60
    if count_sec<=9:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(time_text,text=f"{count_min}:{count_sec}")
    if(count>0):
        global timer
        timer=window.after(10,count_down,count-1)
    else: 
        if (reps%2==0):
            ticks+=1
            tick_string="✔️"*ticks
            tick_label.config(text=tick_string)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window= Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas= Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img= PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
time_text= canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,25,"bold"))
canvas.grid(row=1,column=1)

timer_label=Label(text="Timer",font=(FONT_NAME,50),fg=GREEN,bg=YELLOW)
timer_label.grid(row=0,column=1)

start_button=Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(row=2,column=0)

reset_button=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(row=2,column=2)

tick_label=Label(fg=GREEN,bg=YELLOW)
tick_label.grid(row=3,column=1)



window.mainloop()