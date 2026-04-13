def main():
    greeting = input("Greeting: ")
    greeting = greeting.strip()
    print("$",value(greeting))

def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.rfind("h") == 0:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
