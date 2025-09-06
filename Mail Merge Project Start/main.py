#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/letters/starting_letter.txt") as letter_file, open("./Input/Names/invited_names.txt") as name_file:
    list_names=name_file.readlines()
    lines= letter_file.read()
    for name in list_names: 
        new_name=name.strip()
        personalized_letter= lines.replace("[name]",new_name)
        with open(f"./Output/ReadyToSend/{new_name}.txt","w") as letters_tbsent: 
            letters_tbsent.write(personalized_letter)


