def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            continue
    print(gauge(percentage))


def convert(fraction):
    if "/" not in fraction:
        raise ValueError

    x, y = fraction.split("/")

    if x.startswith(("-", "+")) or y.startswith(("-", "+")):
        raise ValueError

    if not x.isdigit() or not y.isdigit():
        raise ValueError

    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError

    return int((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
