import json
import os
from datetime import datetime

if "data.json" not in os.listdir():
    with open("data.json", "w") as fp:
        json.dump({"bal": 0, "items": [], "hist": []}, fp, indent=4)


def clr_console():
    os.system("cls||clear")


def get_data() -> dict:
    with open("data.json", "r") as fp:
        data = json.load(fp)
    return data


def update_balance(adj: int) -> None:
    new = get_data()
    new['bal'] += adj
    with open("data.json", "w") as fp:
        json.dump(new, fp, indent=4)


def add_history(det: str) -> None:
    new = get_data()
    new['hist'].append(f"{datetime.now()} {det}")
    with open("data.json", "w") as fp:
        json.dump(new, fp, indent=4)


def purchase_item(name: str, price: int) -> None:
    new = get_data()
    new['items'].append({"name": name, "price": price})
    with open("data.json", "w") as fp:
        json.dump(new, fp, indent=4)


def menu():
    print("--------------------\n Welcome to the Dabloons Bank!\n Select an option below to update your balance:")
    print("  1 - I've been given Dabloons")
    print("  2 - I've been robbed")
    print("  3 - I want to check my transactions")
    print("  4 - I've made a purchase")
    print(f" You have {get_data()['bal']} Dabloons\n--------------------")


menu()

while True:
    response = input()
    if response.strip() in "1234":
        break

if response.strip() == "1":
    clr_console()
    print("Sweet! How many?")
    amt = 0
    while True:
        amt = input()
        try:
            amt = int(amt)
        except ValueError:
            continue
        break
    if amt > 100:
        print("Sorry mate. You've just been scammed, it's against the law to give out more than 100 Dabloons at once!")
    else:
        update_balance(amt)
        add_history(f"Given {amt} Dabloons")
        print(f"Cool, you now have {get_data()['bal']} Dabloons!")
elif response.strip() == "2":
    clr_console()
    print("Sucks to be you lol. How much did you lose?")
    while True:
        amt = input()
        try:
            amt = int(amt)
        except ValueError:
            continue
        break
    update_balance(-amt)
    add_history("Robbed of {amt} Dabloons")
    print(f"Oof. Looks like you now only have {get_data()['bal']} Dabloons.")
elif response.strip() == "3":
    clr_console()
    print("INVENTORY:")
    for item in get_data()['items']:
        print(item['name'])
    print("\nTRANSACTIONS:")
    for t in get_data()['hist']:
        print(t)
elif response.strip() == "4":
    clr_console()
    print("Cool, what did you buy?")
    product = input()
    print("And for how much?")
    while True:
        price = input()
        try:
            price = int(price)
        except ValueError:
            continue
        break
    if get_data()['bal'] < price:
        print("You can't afford this item lol, broke ass")
    else:
        update_balance(-price)
        add_history(f"Purchased {product} for {price} Dabloons")
        purchase_item(product, price)
        print(f"You're now the proud owner of a(n) {product}!")
