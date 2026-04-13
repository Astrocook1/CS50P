greeting = input("Greeting: ")
greeting = greeting.strip()
greeting = greeting.lower()
if greeting.startswith("hello"):
    print("$0")
elif greeting.rfind("h") == 0:
    print("$20")
else:
    print("$100")

