import details 
menu=details.MENU
resources=details.resources
profit=0

def check(coffee):
    try:    
        if resources['water']<menu[f'{coffee}']['ingredients']['water']:
            print("Sorry, there is not enough water.")
            return False
        if ((resources['coffee']<menu[f'{coffee}']['ingredients']['coffee'])):
            print("Sorry, there is not enough coffee.")
            return False
        if coffee!='espresso':
            if resources['milk']<menu[f'{coffee}']['ingredients']['milk']: 
                print("Sorry, there is not enough milk.")
                return False
        return True
    except KeyError:
        print("Error: Coffee not found in the menu.")
        return False
            

def money(coffee,profit,resources,menu):
    
    try:
        quarters=float(input("Please insert coins.\nhow many quarters?: "))
        dimes=float(input("how many dimes?: "))
        nickels=float(input("how many nickels?: "))
        pennies=float(input("how many pennies?: "))
        user_coins= quarters*0.25+dimes*0.1+nickels*0.05+pennies*0.01

        if user_coins>=menu[f"{coffee}"]['cost']:
            req_coins=menu[f'{coffee}']['cost']
            change=user_coins-req_coins
            change_round=round(change,2)
            resources['profit']+=req_coins
            
            resources['water']-=menu[f'{coffee}']['ingredients']['water']
            
            if coffee!='espresso':
                resources['milk']-=menu[f'{coffee}']['ingredients']['milk']
            
            resources['coffee']-=menu[f'{coffee}']['ingredients']['coffee']
            
            if change_round>0: 
                print(f"Here is your ${change_round} in change.")
            
            print(f"Here is your {coffee} ☕. Enjoy!")
        
        else: 
            print("Sorry that's not enough money. Money refunded.")

    except ValueError:
        print("Invalid input. Please enter numeric values for coins.")
    except KeyError:
        print("Error: Menu item not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")


def make_coffee(resources,menu,profit,coffee):
    available=check(f'{coffee}')
    if available==True:        
        money(f'{coffee}',profit,resources,menu)

while True: 
    try:
        coffee=input("What would you like? (espresso/latte/cappuccino): ")
        if coffee.lower()=='off':
            break

        elif coffee.lower()=='report':
            print(resources)

        else: 
            if coffee.lower()=='espresso':
                make_coffee(resources,menu,profit,coffee)
            if coffee.lower()=='latte':
                make_coffee(resources,menu,profit,coffee)
            if coffee.lower()=='cappuccino':
                make_coffee(resources,menu,profit,coffee)
        
    except KeyboardInterrupt:
        print("\nProgram interrupted. Shutting down safely.")
        break
    except Exception as e:
        print(f"Unexpected error: {e}")    
        
        
        
        
