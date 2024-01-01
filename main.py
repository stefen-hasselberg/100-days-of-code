from coffee_machine import MENU, resources

# Constants for currency
PENNY   = 0.01
NICKLE  = 0.05
DIME    = 0.10
QUARTER = 0.25


def report(resources, profit):
    
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Profit: ${profit:.2f}")


def check_resources(resources, drink_resources):
    """ 
        Check if we have enough resources to make the drink.  Returns
        True if we can otherwise False if there is not enough resources
    """
    print(resources)
    print(drink_resources)

    for ingredient in drink_resources:
        if resources.get(ingredient) < drink_resources.get(ingredient):
            print(f"Sorry, there is not enough {ingredient}")
            return False
        
        return True           
            
def calculate_payment():
    """
    # ask the user for payment of the drink by asking them to insert coins, pennies, dimes, nickles, quarters
    # calculate the payment
    """    
    try:
        print("Please insert coins")
        quarters = int(input("how many quarters?: "))
        dime = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))

        return (quarters * QUARTER) + (dime * DIME) + (nickles * NICKLE) + (pennies * PENNY)
    except:
        print("Invalid input please only enter numbers")
        calculate_payment()


def make_drink(resources, ingredients):

    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    
    return resources

# TODO
#  Turn coffee machine on
status = "on"
profit = 0

while status == "on":
    
    
    # TODO 1
    #  ask user for selection
    selection = input("What would you like? (espresso/latte/cappuccino):")
    
    if selection in MENU.keys():

        drink = MENU[selection]

        # TODO 4
        #  if user selects a drink we need to check that we have enough resources to make the drink
        #  if we don't have enough resources then we need print a message "Sorry there is not enough [resource]"

        if check_resources(resources, drink['ingredients']):           
            
            # TODO 6
            # check that users has enter enough coins to pay for the drink, if it's not enough then pring a message
            # sorry not enough 
            payment = calculate_payment()

            if payment >= drink['cost']:
                print("making drink")

                # TODO 7
                # if the user has paid enough then the cost of the drink gets add to the machines profit
                # if the user has enter too much then offer change
                profit += drink['cost']

                # TODO 8
                # reduce the resources by subtracting the resources it takes to make the drink
                resources = make_drink(resources, drink['ingredients'])

                print("here is your drink ☕ ")
                
                if payment > drink['cost']:
                    change = payment - drink['cost']
                    print(f"Here is ${change:.2f} dollars in change")

            else:
                print("Sorry that's not enough money. Money refunded")
                continue

        else:
            continue


    elif selection == "report":
        report(resources, profit)
    elif selection == "off":
        print("Turning machine off")
        status = "off"
    else:
        print(f"Unknown selection please choose from (espresso/latte/cappuccino):")





