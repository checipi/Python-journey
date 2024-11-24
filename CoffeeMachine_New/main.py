from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine




money_machine = MoneyMachine()
coffee_machine = CoffeeMaker()
menu = Menu()

def main():
    machine_on = True
    while machine_on:
        choice = input(f"Choose a drink {menu.get_items()}: ").lower()
        if choice == "off":
            machine_on = False
        elif choice == "report":
            money_machine.report()
            coffee_machine.report()
        else:
            drink = menu.find_drink(choice)
            if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
                
if __name__ == "__main__":
    main()
        
