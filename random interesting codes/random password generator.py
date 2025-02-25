import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)
list_of_characters=[letters,numbers,symbols]
shuffled_list_of_characters=[]
for i in range(0,26):
    shuffled_list_of_characters+=list_of_characters[random.randrange(0,random.randrange(1,4))][random.randrange(1,9)]
print(shuffled_list_of_characters)

#now for the actual password, for which we will take elements from shuffled_list_of_characters. 
pc=''
for i in range(1,random.randrange(4,len(shuffled_list_of_characters))): 
    pc+=shuffled_list_of_characters[i]
print(f"The randomly generated passcode is- {pc}")


