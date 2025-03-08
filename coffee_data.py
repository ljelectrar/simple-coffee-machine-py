options = ["espresso","latte", "cappuccino"]
ingredients = ["water", "coffee", "milk", "chocolate"]
coins = {
    "pennie": 0.01,
    "nickle": 0.05,
    "dime": 0.10,
    "quarter": 0.25,
}
resources = {
    ingredients[0]: 1000, # water
    ingredients[1]: 500, # coffee
    ingredients[2]: 1000, # milk
    ingredients[3]: 500, # chocolate
    "money": 0
}

drinks = {
    # expresso
    options[0]: {
        ingredients[0]: 200,
        ingredients[1]: 25,
        "price": 1
    },
    # latte
    options[1]: {
        ingredients[0]: 200,
        ingredients[1]: 25,
        ingredients[2]: 200,
        "price": 2.5
    },
    # capuccino
    options[2]: {
        ingredients[0]: 200,
        ingredients[1]: 25,
        ingredients[2]: 200,
        ingredients[3]: 25,
        "price": 3.5
    }
}