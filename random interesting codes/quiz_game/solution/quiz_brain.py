class QuizBrain: 
    def __init__(self,list_question):
        self.question_number=0 
        self.question_list= list_question
        self.score=0
    
    def next_question_(self):
        current_question= self.question_list[self.question_number]
        self.question_number+=1
        ans= input(f"Q.{self.question_number}: {current_question.q_text} (True/False)?: ")
        self.check_answer(ans,current_question.q_answer)
    
    def still_has_questions(self): 
        return self.question_number!=len(self.question_list)
    
    def check_answer(self,user_ans,comp_ans):
        if user_ans.lower()==comp_ans.lower():
            print("You got it right!")
            self.score+=1
        else: 
            print("You got it wrong!")
        print(f"The correct answer was: {comp_ans}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")