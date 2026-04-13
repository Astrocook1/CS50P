import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.match(r"^(\d+):?(\d+)? (AM|PM) to (\d+):?(\d+)? (AM|PM)$", s)
    if matches:
        for m in matches.groups():
            if not(m == None) and len(m) > 2:
                raise ValueError
        times = []
        for i in range(1,5,3):
            if int(matches.group(i)) < 1:
                raise ValueError

            time = {"hour":0 if matches.group(i) == "12" else int(matches.group(i)),
            "minutes":0 if matches.group(i+1) == None else int(matches.group(i+1)),
            "meridiem":0 if matches.group(i+2) == "AM" else 12}

            if time["hour"] > 12:
                raise ValueError
            if time["minutes"] > 59 or time["minutes"]< 0:
                raise ValueError
            times.append(time)

        return(f"{times[0]["hour"] + times[0]["meridiem"]:02}:{times[0]["minutes"]:02} to {times[1]["hour"] + times[1]["meridiem"]:02}:{times[1]["minutes"]:02}")
    else:
        raise ValueError


if __name__ == "__main__":
    main()
