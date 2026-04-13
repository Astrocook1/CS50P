import sys
import csv
from tabulate import tabulate


if (len(sys.argv) - 1) < 1:
    sys.exit("Too few command-line arguments")
elif (len(sys.argv) - 1) > 1:
    sys.exit("Too many command-line arguments")

menu = sys.argv[1].lstrip()
if not(menu.endswith(".csv")):
    sys.exit("Not a CSV file")

menu_list = []

try:
    with open(menu) as menu:
        reader = csv.reader(menu)
        for row in reader:
            menu_list.append(row)

except(FileNotFoundError):
    sys.exit("File does not exist")

print(tabulate(menu_list, headers = "firstrow", tablefmt = "grid"))
