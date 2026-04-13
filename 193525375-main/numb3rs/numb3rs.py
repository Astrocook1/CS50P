import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.match(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if matches:
        for i in range (len(matches.groups())):
            check = re.search("^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$", matches[i+1])
            if not check:
                return False

        return True
    else:
        return False


if __name__ == "__main__":
    main()
