def main():
    text = input("Input: ")
    text = text.strip()
    text = shorten(text)
    print(text)

def shorten(word):
    list = []
    for i in range(len(word)):
        match word[i]:
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
        list.append(word[i])
    word = "".join(list)
    return word


if __name__ == "__main__":
    main()
