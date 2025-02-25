import random 
user_no=int(input("Enter rock,paper or scissors (0,1 or 2)"))
computer_no= random.randrange(0,3) #0,1,2
print(user_no)
print(computer_no)
if user_no==0: 
    print('''User chose
       _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    (rock)                            ''')

elif user_no==1: 
    print('''User chose
        _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    (paper)                            ''')

elif user_no==2: 
    print('''User chose
        _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    (scissors)                            ''')
else: 
    print("The number you have entered is invalid.") 
if computer_no==0: 
    print('''Computer chose
       _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    (rock)                            ''')

elif computer_no==1: 
    print('''Computer chose
        _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    (paper)                            ''')

elif computer_no==2: 
    print('''Computer chose
        _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    (scissors)                            ''')

if user_no==0: 
    if computer_no==0: #rock and rock 
        print("No one wins")
    elif computer_no==1: #rock and paper
        print("Computer wins")
    elif computer_no==2: #rock and scissors
        print("User wins")
elif user_no==1: 
    if computer_no==0: #paper and rock 
        print("User wins")
    elif computer_no==1: #paper and paper
        print("No one wins")
    elif computer_no==2: #paper and scissors
        print("Computer wins")
elif user_no==2: 
    if computer_no==0: #scissors and rock 
        print("Computer wins")
    elif computer_no==1: #scissors and paper
        print("User wins")
    elif computer_no==2: #scissors and scissors
        print("No one wins")
