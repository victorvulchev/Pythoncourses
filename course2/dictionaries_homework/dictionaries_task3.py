menu = {"sandwich":10,
        "tea" : 7}

order = input("What would you like to order:")
total = 0
while True:
    if order in menu:
        total += menu.get(order)
        print(f"{order} costs {menu.get(order)}, total is {total}")
        order = input("Anything else?")
    else:
        print(f"Sorry, we are fresh out of {order} today.")
        order = input("Anything else?")

    if order == "no":
        print(f"Your total is {total}")
        break
