#key logic.. to wrap around the list without having to check if index goes out of range, modulus operator can be used. %%%%%%%%%%%%. 

print('''\n\n ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
'"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
'"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88            \n\n''')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
'r', 's', 't', 'u', 'v', 
'w', 'x', 'y', 'z']
cap_letters= [letter.upper() for letter in letters]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','10']
go=True
def caesar(type,msg,shift): 
        emp= ''
        if type=='decode':
            shift*=-1
        for char in range(len(msg)): 
            if msg[char] in letters: 
                index_char= letters.index(msg[char])
                emp+= letters[(index_char+shift) % len(letters)]
                
            
            elif msg[char] in cap_letters: 
                index_char= cap_letters.index(msg[char])
                emp+= cap_letters[(index_char+shift)%len(cap_letters)]
            elif msg[char]==' ': 
                emp+=' '
            else: 
                index_char= numbers.index(msg[char])
                emp+= numbers[(index_char+shift)%len(numbers)]
        print(emp)           
while go:
    type_= input("Type 'encode' to encrypt, and 'decode' to decrypt: \n")
    msg= input('Type your message:\n')
    shift= int(input('Type the shift number:\n'))
    caesar(type_,msg,shift)
    choice= input('Do you want to continue (yes/no):\n')
    if choice.lower()=='no': 
        go=False

