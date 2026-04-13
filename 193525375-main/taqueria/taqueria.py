price = 0
while True:
    try:
        while True:
            item = input("Item: ")
            item = item.strip()
            item = item.title()
            menu = {
            "Baja Taco": 4.25,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
            }
            price += menu[item]
            print("Total: $%.2f" % (price))
    except KeyError:
        pass
    except EOFError:
        break
