import logo 
import random
print(logo.logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
diff=input("Choose a difficulty. Type 'easy' or 'hard': ")

random_number=random.randrange(1,101)

def guess():
    global random_number
    guess=int(input("Make a guess: "))
    if guess==random_number:
        print(f"You got it! The answser was {guess}")
        return 0
    if guess>random_number:
        print("Too high, guess again!")
    else:
        print("Too low, guess again!")

if diff=='easy':
    print("You have 10 attempts to guess the number.")
    for i in range(1,11):
        guess()
        if guess()==0:
            break
if diff=='hard':
    print("YOu have 5 attempts to guess the number.")
    for i in range(1,6):
        guess()
        if guess()==0:
            break