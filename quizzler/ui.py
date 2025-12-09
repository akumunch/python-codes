from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT= ("Arial",20,"italic")

class QuizInterface():
    def __init__(self,quiz:QuizBrain):
        self.score=0
        self.window=Tk()
        self.quiz=quiz
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_label= Label(text=f"Score: {self.score}",bg=THEME_COLOR,fg="white")
        self.score_label.grid(row=0,column=1,pady=5)

        self.canvas_q= Canvas(width=300,height=250)
        self.question_text= self.canvas_q.create_text(
                150,
                125,
                width=280,
                fill=THEME_COLOR,text="Some question",
                font=FONT)
        self.canvas_q.grid(row=1,column=0,columnspan=2)

        true_image= PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image,command=self.func_true,highlightthickness=0,bg= THEME_COLOR)
        self.true_button.grid(row=2,column=0,pady=8)

        false_image= PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image,command=self.func_false,highlightthickness=0,bg=THEME_COLOR)
        self.false_button.grid(row=2,column=1,pady=8)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text= self.quiz.next_question()
            self.score_label.config(text= f"Score: {self.quiz.score}")
            self.canvas_q.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas_q.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def func_true(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def func_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
    
    def give_feedback(self,is_right: bool):
        if is_right: 
            self.canvas_q.config(bg="green")
        else: 
            self.canvas_q.config(bg="red")
        self.window.after(1000,lambda: (self.change_white(),self.get_next_question()))
    
    def change_white(self):
        self.canvas_q.config(bg="white")
    