def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif s[0].isdigit() or s[1].isdigit():
        return False
    elif not(s[0].isalnum()) or not(s[1].isalnum()):
        return False
    else:
        return (check(s))

def check(s):
    count = 0
    for i in range(2,len(s)):
        if not(s[i].isalnum()):
            return False
        else:
            if i < (len(s) - 1):
                 if s[i].isdigit():
                    count += 1
                    if s[i] == "0" and count == 1:
                        return False
                    elif (check_for_mid_alphabets(s[i+1:(len(s))])):
                        return False

    return True

def check_for_mid_alphabets(t):
    for i in range(len(t)):
        if t[i].isalpha():
            return True

if __name__ == "__main__":
    main()
