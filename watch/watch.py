import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.match(r"^<iframe.*src=\"(.+)\".*></iframe>$", s)
    if matches:
        matches1 = re.match(r"^https?://w{0,3}\.?youtube\.com/embed(/.+)$", matches.group(1))
        if matches1:
            return(f"https://youtu.be{matches1.group(1)}")
        else:
            return None
    else:
        return None

...


if __name__ == "__main__":
    main()
