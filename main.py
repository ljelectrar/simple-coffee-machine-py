from numbers import Number

from coffee_data import options, ingredients, resources, drinks, coins

# imported:
# 1. options - list
# 2. ingredients - list
# 3. resources - dictionary
# 4. drinks - dictionary
# NOTE: items 3 and 4 are compositions/combinations of options, and ingredients

# TODO 5. Process coins
def process_coins(command):
    drink_value = drinks[command]["price"]
    coins_inserted = []
    coins_sum = 0.0

    while coins_sum < drink_value:
        coin = input(
            f"Enter your coins to purchase your drink: price:${drink_value}\n($ accepts: pennie, nickle, dime, quarters)\ntype 'enter' to validate the value, 'cancel' to exit")
        if coin == "cancel":
            return init()
        if coin == "enter":
            print("\n::::::::: You didn't insert any coin yet... please, try again. :::::::::\n")
            return process_coins(command)

        if coin == "pennie":
            coins_inserted.append(coins["pennie"])
            coins_sum += coins['pennie']
            print(coins_sum)

        elif coin == "nickle":
            coins_inserted.append(coins["nickle"])
            coins_sum += coins['nickle']
            print(coins_sum)

        elif coin == "dime":
            coins_inserted.append(coins["dime"])
            coins_sum += coins['dime']
            print(coins_sum)

        elif coin == "quarter":
            coins_inserted.append(coins["quarter"])
            coins_sum += coins['quarter']
            print(coins_sum)

        else:
            print("Please, try again with a valid coins!")
            print(f"error! Here's your coins back {coins_inserted}")
            return init()

    if coins_sum >= drink_value:
        make_coffee(command)
    else:
        return init()

# TODO 7. Make coffee
def make_coffee(drink):
    if drink == 'espresso':
        resources['water'] -= drinks['espresso']['water']
        resources['coffee'] -= drinks['espresso']['coffee']
        resources['money'] += drinks['espresso']['price']

    elif drink == 'latte':
        resources['water'] -= drinks['latte']['water']
        resources['coffee'] -= drinks['latte']['coffee']
        resources['milk'] -= drinks['latte']['milk']
        resources['money'] += drinks['latte']['price']

    elif drink == 'cappuccino':
        resources['water'] -= drinks['cappuccino']['water']
        resources['coffee'] -= drinks['cappuccino']['coffee']
        resources['milk'] -= drinks['cappuccino']['milk']
        resources['chocolate'] -= drinks['cappuccino']['chocolate']
        resources['money'] += drinks['cappuccino']['price']

    else:
        print("Some error happen! please, try again!")
        return init()

    print(f"Sucessfull: here is your drink: {drinks[drink]}")
    return init()

def report():
    for item in resources:
        print(f"{item}: {resources[item]}")
    return init()

def check_resources(drink):
    if drink == "espresso":
        if resources["water"] < drinks[drink]["water"] or resources["coffee"] < drinks[drink]["coffee"]:
            print(f"There's no resource available to make this {drink}")
            return init()


    elif drink == "latte":
        if resources["water"] < drinks[drink]["water"] or resources["coffee"] < drinks[drink]["coffee"] or resources["milk"] < drinks[drink]["milk"]:
            print(f"There's no resource available to make this {drink}")
            return init()

    elif drink == "cappuccino":
        if resources["water"] < drinks[drink]["water"] or resources["coffee"] < drinks[drink]["coffee"] or resources["milk"] < drinks[drink]["milk"] or resources["chocolate"] < drinks[drink]["chocolate"]:
            print(f"There's no resource available to make this {drink}")
            return init()

    else:
        print("returning to main menu... sorry!")
        return init()


# TODO 1. Prompt user by asking "What would you like?" (espresso/latte/cappuccino)
def init():
    command = input("What would you like? (espresso/latte/cappuccino)")
    while command != options[0] and command != options[1] and command != options[2]:
        # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
        if command == "off":
            print("You turn off the Coffee Machine... (command == 'off')")
            break
        # TODO 3. Print report (resources) by entering "report" to the prompt.
        if command == "report":
            report()

        print("------ DRINK ERROR ------ Please, select a valid drink.")
        command = input("What would you like? (espresso/latte/cappuccino)")
    # TODO 4. Check if are resources sufficient?
    check_resources(command)
    process_coins(command)

# TODO 6. Check if is transaction successful

if __name__ == '__main__':
    init()