import cont
print(cont.logo)

auction_bids={} # in general of form 'name':bid ; 
while True: 
    name= input("What is your name?: ")
    bid=int(input("What is your bid?: "))
    auction_bids={name:bid}
    while True:
        check_ = input("Are there any other bids (yes/no)? ").strip().lower()
        check=check_.strip().lower()
        # Check if the input is valid
        if check == 'yes' or check_ == 'no':
            break  # Exit the loop if the input is valid
        else:
            print("Invalid input, please enter 'yes' or 'no'.")  # Prompt for valid input

    if check=='yes': 
        print("\n"*100)
        continue
    elif check=='no': 
        max_name=max(auction_bids,key=auction_bids.get)
        max=auction_bids[max_name] 
        #now max will have the max bidding value. 
        print(f"The winner is {max_name} with a bid of {max}.")
        break