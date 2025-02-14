import logo 
import random

cards=[1,2,3,4,5,6,7,8,9,10,'A','J','Q','K']
your_cards=random.choices(cards,k=2) #gives 2 random choices from cards

computer_card=random.choice(your_cards)
if isinstance(computer_card,str):
    computer_card=10
#print(your_cards)

for i in range(len(your_cards)): 
    if isinstance(your_cards[i],str):
        your_cards[i]=10

score=sum(your_cards)
#print(your_cards) #now your cards has the user pair of nos. 


while True: 
    while True:
        ans=input("Do you want to play a game of blackjack? (y/n): ")
        if ans.lower() in 'yn':
            break
        else: 
            print("Invalid input, enter y/n: ")
    if ans: 
        print(logo.logo)
        print(f"Your cards: {your_cards}, current score: {score}")
        print(f"Computer's first card: {computer_card}")
        while True: 
            print("Type 'y' to ")