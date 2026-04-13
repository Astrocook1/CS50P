expression = input("Expression: ")
expression = expression.strip()
list = expression.split(" ")
x = float(list[0])
y = list[1]
z = float(list[2])
match y:
    case "+":
        print(x+z)
    case "-":
        print(x-z)
    case "/":
        print(x/z)
    case "*":
        print(x*z)
    case _:
        print("Invalid expression")
