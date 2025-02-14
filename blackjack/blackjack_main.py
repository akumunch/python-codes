import logo 
import random

while True: 
    
    while True:
        ans=input("Do you want to play a game of blackjack? (y/n): ")
        if ans.lower() in 'yn':
            break
        else: 
            print("Invalid input, enter y/n: ")
    
    if ans.lower()=='y': 
        print(logo.logo)
        cards=[2,3,4,5,6,7,8,9,10,'A','J','Q','K']
        your_cards=random.choices(cards,k=2) #gives 2 random choices from cards
        computer_card=[]
        computer_card.append(random.choice(cards))

        for i in range(len(computer_card)): 
            if isinstance(computer_card[i],str):
                computer_card[i]=10
        for i in range(len(your_cards)): 
            if your_cards[i]!='A':
                your_cards[i]=10
            else: 
                your_cards[i]=int(input("Do you want your A to be 1/11? "))
        score=sum(your_cards)
        print(f"Your cards: {your_cards}, current score: {score}\n")
        print(f"Computer's first card: {computer_card}\n") 
        while score<21:
            while True:
                cont=input("Type 'y' to get another card, type 'n' to pass: ")
                if cont.lower() in 'yn':
                    break
                else: 
                    print("Invalid input, enter y/n: ")
            if cont.lower()=='y':
                extra_card=random.choice(cards)
                if isinstance(extra_card,str):
                    if extra_card!='A':
                        extra_card=10
                    else:
                        extra_card=int(input("Do you want your A to be 1/11? "))
                your_cards.append(extra_card)
                score=sum(your_cards)
                print(f"Your cards: {your_cards}, current score: {score}\n")
                print(f"Computer's first card: {computer_card}\n") 
                if score==21:
                    print("Blackjack! You win!")
                    break
                if score>sum(computer_card):
                    print("You win!")
                    break
            else: #user does not want to pick another card and their score is lesser than 21  
                #so now we have to compare user's and computer's scores after handing computer another card. 
                computer_card.append(random.choice(your_cards))
                for i in range(len(computer_card)): 
                    if isinstance(computer_card[i],str):
                        computer_card[i]=10
                print(f"Your final hand: {your_cards}, final score: {sum(your_cards)}"
                f"\nComputer's final hand: {computer_card}, final score: {sum(computer_card)}")
                if score>sum(computer_card):
                    print("You win, you have more points.")
                    break
                elif sum(computer_card)>21:
                    print("You win, computer exceeded 21 points.")
                    break
                elif score<sum(computer_card): 
                    print("You lose, computer has more points.")
                    break
        #now, user's score is more than 21 so user loses. 
        if score>21:
            print(f"Your cards: {your_cards}, current score: {sum(your_cards)}"
        f"\nComputer's first card: {computer_card}"
        f"\nYou went over, you lose 😭!")
    else: 
        break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    























    
    
    
    
