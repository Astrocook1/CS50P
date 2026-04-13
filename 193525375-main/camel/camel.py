camel = input("camelCase:")
camel = camel.strip()
list = []
for i in range(len(camel)):
    list.append(camel[i])
for i in range(len(camel)):
    if list[i].isupper():
        list[i] = list[i].lower()
        list.insert(i,"_")
        continue

snake = "".join(list)
snake = snake.strip()
print(snake)
