from random import randint
while True:
    try:
        while True:
            level = int(input("Level:"))
            if level >= 1:
                break
        break
    except ValueError:
        continue

integer = randint(1,level)

while True:
    try:
        while True:
            guess = int(input("Guess: "))
            if guess < 1:
                continue
            if guess == integer:
                print("Just right!")
                break
            elif guess < integer:
                print("Too small!")
                continue
            elif guess > integer:
                print("Too large!")
                continue

    except ValueError:
        continue
    else:
        break
