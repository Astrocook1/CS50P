def main():
    time = input("What time is it? ")
    time = time.strip()
    time = convert(time)
    if time >= 7 and time <= 8:
        print("Breakfast time")
    elif time >= 12 and time <= 13:
        print("Lunch time")
    elif time >= 18 and time <= 19:
       print("Dinner time")
    else:
        exit
def convert(time):
    list = time.split(":")
    hour = float(list[0])
    minute = float(list[1])
    minute = minute / 60
    return (hour + minute)

if __name__ == "__main__":
    main()
