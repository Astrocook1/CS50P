def main():
    sentence = input()
    face = convert(sentence)
    print(face)

def convert(str):
    output = str.replace(":)","🙂")
    output1 = output.replace(":(","🙁")
    return output1

main()
