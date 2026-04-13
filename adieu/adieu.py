import inflect
p = inflect.engine()
greeting = ("Adieu, adieu, to ")
names = []

try:
    while (True):
        name = input("Name: ")
        names.append(name)
except EOFError:
    print("")

print(greeting + p.join((names)))
