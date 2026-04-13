paid = 0
while paid < 50:
    due = 50 - paid
    print("Amount Due:",due)
    coin = eval(input("Insert Coin: "))
    if coin == 25 or coin == 10 or coin == 5:
        paid += coin
        print(paid)
    else:
        continue

print("Change Owed:",paid - 50)

