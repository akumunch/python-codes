import pandas
student_data_frame = pandas.read_csv("C:/Users/USER/Desktop/python-codes/day_26/myenv/NATO-alphabet-start/nato_phonetic_alphabet.csv")

dict= {value.letter:value.code for (key,value) in student_data_frame.iterrows()}
word= input("Enter word: ").upper()
lst= [dict[letter] for letter in word]
print(lst)


