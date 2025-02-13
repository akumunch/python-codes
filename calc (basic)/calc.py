import logo
print(logo.calc_logo)

def addition(num1,num2):
    return num1+num2 
def subtraction(num1,num2): 
    return num1-num2
def multiplication(num1,num2): 
    return num1*num2
def division(num1,num2):
    return num1/num2

while True: 
    num1=float(input("What's the first number?: "))
    operations="+\n-\n*\n/"
    while True:    
        operation=input("Pick an operation: +\n-\n*\n/\n")
        if operation=='+' or operation=='-' or operation=='*' or operation=='/': 
            break
        else:
            print("Invalid input.") 
            continue 
    num2= float(input("What's the next number?: "))
    if operation=='+': 
        print(addition(num1,num2))
    elif operation=='-': 
        print(subtraction(num1,num2))
    elif operation=='*':
        print(multiplication(num1,num2))
    else:
        print(division(num1,num2))
    