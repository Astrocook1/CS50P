text = input("Input: ")
text = text.strip()
list = []
for i in range(len(text)):
    match text[i]:
        case "a":
            continue
        case "e":
            continue
        case "i":
            continue
        case "o":
            continue
        case "u":
            continue
        case "A":
            continue
        case "E":
            continue
        case "I":
            continue
        case "O":
            continue
        case "U":
            continue
    list.append(text[i])
text = "".join(list)
print(text)
