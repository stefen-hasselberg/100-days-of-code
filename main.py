from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

status = True

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while status:

    options = menu.get_items()

    drink_selection = input(f"What would you like, ({options})")

    if drink_selection == 'report':
        coffee_maker.report()
        money_machine.report()
    elif drink_selection == "off":
        print("Shutting down")
        status = False
    else:
        drink = menu.find_drink(drink_selection)
        
        # check that we got enough resources to make drink
        if coffee_maker.is_resource_sufficient(drink):
            
            if money_machine.make_payment(drink.cost):

                coffee_maker.make_coffee(drink)

