MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def calculate_coins(_quarters, _dimes, _nickles, _pennies):
    times_quarters = _quarters * 0.25
    times_dimes = _dimes * 0.10
    times_nickles = _nickles * 0.05
    times_pennies = _pennies * 0.01

    result = times_quarters + times_dimes + times_nickles + times_pennies
    return result

def difference_with_price(_amount):
    total_amount = _amount

    difference = 0
    type_price = 0
    if answer == "latte":
        type_price = 2.50
        difference = _amount - type_price
    elif answer == "espresso":
        type_price = 1.50
        difference = _amount - type_price
    elif answer == "cappuccino":
        type_price = 3
        difference = _amount - type_price

    if difference >= 0:
        print(f"Here is ${difference:.2f} in change")
        print(f"Here is your {answer} ☕️. Enjoy!")
        return True
    if difference < 0:
        print(f"Price: ${type_price:.2f} // ${total_amount:.2f} is not enough. Money refunded")
        return False

def decrease_original_resources(user_input, original_resources):
    type_of_coffee_ingredients = MENU[user_input]
    water = type_of_coffee_ingredients["ingredients"]["water"]

    milk = 0
    if answer != "espresso":
        milk = type_of_coffee_ingredients["ingredients"]["milk"]

    coffee = type_of_coffee_ingredients["ingredients"]["coffee"]

    original_water = original_resources["water"]
    original_milk = original_resources["milk"]
    original_coffee = original_resources["coffee"]

    new_water = original_water - water
    new_milk = original_milk - milk
    new_coffee = original_coffee - coffee

    resources["water"] = new_water
    resources["milk"] = new_milk
    resources["coffee"] = new_coffee

    return new_water, new_milk, new_coffee

def check_ingredients(user_input, original_resources):
    original_water = original_resources["water"]
    original_milk = original_resources["milk"]
    original_coffee = original_resources["coffee"]

    type_of_coffee_ingredients = MENU[user_input]
    water = type_of_coffee_ingredients["ingredients"]["water"]
    milk = 0
    if answer != "espresso":
        milk = type_of_coffee_ingredients["ingredients"]["milk"]
    coffee = type_of_coffee_ingredients["ingredients"]["coffee"]

    if original_water < water:
        return "no water"
    elif original_milk < milk:
        return "no milk"
    elif original_coffee < coffee:
        return "no coffee"

should_continue = True
while should_continue:
    answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
    print()
    if answer == "off":
        should_continue = False
    elif check_ingredients(answer,resources) == "no water":
        print("There's not enough Water. Please add more Water")
        print()
    elif check_ingredients(answer,resources) == "no milk":
        print("There's not enough Milk. Please add more Milk")
        print()
    elif check_ingredients(answer,resources) == "no coffee":
        print("There's not enough Coffee. Please add more Coffee")
        print()
    else:
        new_resources = decrease_original_resources(answer, resources)

        after_water = new_resources[0]
        after_milk = new_resources[1]
        after_coffee = new_resources[2]

        print("Please insert coins: ")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        print()

        amount = calculate_coins(quarters,dimes,nickles,pennies)

        change_or_not = difference_with_price(amount)

        print("\n" * 5)