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

money = 0


def coins(coffee):
    print("Please insert coins.")
    a = float(input("how many quarters?: "))
    b = float(input("how many dimes?: "))
    c = float(input("how many nickels?: "))
    d = float(input("how many pennies?: "))
    total = (0.25 * a) + (0.10 * b) + (0.05 * c) + (0.01 * d)
    cost_of_coffee = MENU[coffee]["cost"]
    if cost_of_coffee > total:
        print("Sorry, that's not enough money. Money refunded.")
    elif cost_of_coffee <= total:
        change = round(abs(cost_of_coffee - total), 2)
        global money
        money += cost_of_coffee
        print(f"Here is ${change} in change.")
        print(f"Here is your {coffee} ☕.️ Enjoy!")


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        return True


def resources_left(order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")


coffee_is_on = True

while coffee_is_on:
    place_order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if place_order == "report":
        resources_left(MENU[place_order]["ingredients"])
        print(f"Money: ${money}")
    elif place_order == "espresso":
        if is_resource_sufficient(MENU["espresso"]["ingredients"]):
            coins("espresso")
    elif place_order == "latte":
        if is_resource_sufficient(MENU["latte"]["ingredients"]):
            coins("latte")
    elif place_order == "cappuccino":
        if is_resource_sufficient(MENU["cappuccino"]["ingredients"]):
            coins("cappuccino")
    elif place_order == "off":
        coffee_is_on = False
    else:
        print("Enter a valid order.")
