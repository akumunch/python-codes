import pandas
student_data_frame = pandas.read_csv("C:/Users/USER/Desktop/python-codes/day_26/myenv/NATO-alphabet-start/nato_phonetic_alphabet.csv")

dict= {value.letter:value.code for (key,value) in student_data_frame.iterrows()}

while(1):
    word= input("Enter word: ").upper()

    try:
        lst= [dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else: 
        print(lst)
        break

