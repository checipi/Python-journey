from MENU import MENU
import os
from time import sleep


resources = {
    "water":300,
    "milk": 200,
    "coffee": 100,
}


money = {
    "value": 0,
}

def display_report():
    """Displays a report onthe screen with the resources and money in the machine."""
    print("\nResources:")
    for resource in resources:
        if resource == "coffee":
            print(f"{resource.title()}: {resources[resource]}g")
        else:
            print(f"{resource.title()}: {resources[resource]}ml")
    print(f"Money: ${money['value']}\n")
        
def check_resources(s):
    coffee_resources = MENU[s]['ingredients']
    for resource in coffee_resources:
        if coffee_resources[resource]>resources[resource]:
            print(f"Sorry, there is not enough {resource}")
            return 0
        else:
            return coffee_resources


def insert_money():
    """Calculates the inserted sum of money in dollars"""
    print("Please insert coins:")
    try:
        pennies = float(input("Insert pennies: "))
        nickles = float(input("Insert nickles: "))
        dimes = float(input("Insert dimes: "))
        quarters = float(input("Insert quarters: "))
        money = pennies*0.01 + nickles*0.05 + dimes*0.10 + quarters*0.25
        print("Type",type(money))
        return money
    except ValueError:
        print("Wrong button. Try again.")
        return insert_money()


def main():
    machine_on = True
    while machine_on:    
        user_choice = input("What would you like? (espresso/latte/cappucciono): ").lower()
        if user_choice == "off":
            machine_on = False
        elif user_choice == "report":
            display_report()
        elif user_choice in MENU:
            cof_resources  = check_resources(user_choice)
            if cof_resources == 0:
                continue
            ask_money = float("%.2f"%insert_money())
            # print("Money:",ask_money)
            while ask_money < MENU[user_choice]['cost']:
                print(f"Sorry, that's not enough money. Ammount refunded.")
                ask_money = float("%.2f"%insert_money())  
                # print("Money:",ask_money)    
            print(f"Here is the change: ${"%.2f"%(ask_money-MENU[user_choice]['cost'])}")
            money["value"] += ask_money
            for resource in cof_resources:
                resources[resource] -= cof_resources[resource]
            print("Please take your coffee.\nHave a nice day!")
            sleep(3)
            os.system("cls")
            
if __name__ == "__main__":
    main()
