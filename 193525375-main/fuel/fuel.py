while True:
    try:
        fraction = input("Fraction: ")
        fraction = fraction.strip()
        if not("/" in fraction):
            continue
        num_list = fraction.split("/")
        x = int(num_list[0])
        y = int(num_list[1])
        if x > y or x < 0 or y < 0 :
            continue
        percentage = (((x / y) * 100))

    except ValueError:
        continue
    except ZeroDivisionError:
        continue
    else:
        break


if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(round(percentage),"%",sep = "")
