import sys

if (len(sys.argv) - 1) < 1:
    sys.exit("Too few command-line arguments")
elif (len(sys.argv) - 1) > 1:
    sys.exit("Too many command-line arguments")

title = sys.argv[1].lstrip()
if not(title.endswith(".py")):
    sys.exit("Not a python file")

count = 0

try:
    with open(title) as file:
        for line in file:
            line = line.strip()
            if line.startswith("#"):
                continue
            elif line == "":
                continue
            else:
                count +=1

except(FileNotFoundError):
    sys.exit("File does not exist")


print(count)
