import game_logo,game_data,random
print(game_logo.header)

score=0

while True: 
    random_no_1=random.randint(0,len(game_data.data)-1)
    random_no_2=random.randint(0,len(game_data.data)-1)
    print(f"Compare A: {game_data.data[random_no_1]['name']},a {game_data.data[random_no_1]['description']},from {game_data.data[random_no_1]['country']}")
    print(f"\n{game_logo.vs}\n")
    print(f"Against B: {game_data.data[random_no_2]['name']},a {game_data.data[random_no_2]['description']},from {game_data.data[random_no_2]['country']}")

    input_=input("Who has more followers, A or B? ")
    if game_data.data[random_no_1]['follower_count']>game_data.data[random_no_2]['follower_count']:
        check=0
    else: 
        check=1
    if input_=='A' and check==0:
        print(f"You got it right. Score+=1")
        score+=1
    elif input_=='B' and check==1:
        print(f"You got it right. Score+=1")
        score+=1
    else: 
        print(f"Sorry, that's wrong. Final score: {score}")
        break