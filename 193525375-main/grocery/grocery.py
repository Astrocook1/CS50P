count = 0
list = []
while True:
    try:
        item = input("")
        item = item.strip()
        item = item.upper()
        list.append(item)
    except EOFError:
        break

for i in sorted(set(list)):
    print(list.count(i), i)
