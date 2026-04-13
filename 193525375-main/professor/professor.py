import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        j = 0
        while j < 3:
            try:
                k = eval(input(f"{x} + {y} = "))
            except NameError:
                pass
            if k == z:
                print("a")
                score += 1
                break
            elif j == 2:
                print((f"{x} + {y} = {z}"))
                break
            else:
                print("EEE")
                j += 1
                continue
    print("Score:",score)


def get_level():
    while True:
        try:
            level = eval(input("Level: "))
        except NameError:
            pass
        try:
            if (level >= 1  and level <=3):
                break
        except UnboundLocalError:
            pass
    return level

def generate_integer(level):
    if level == 1:
        return(random.randint(0,9))
    elif level == 2:
        return(random.randint(10,99))
    elif level == 3:
        return(random.randint(100,999))
    else:
        raise ValueError


if __name__ == "__main__":
    main()
