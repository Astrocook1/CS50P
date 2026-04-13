import sys
import csv

if (len(sys.argv) - 1) < 2:
    sys.exit("Too few command-line arguments")
elif (len(sys.argv) - 1) > 2:
    sys.exit("Too many command-line arguments")

before = sys.argv[1].strip()
after = sys.argv[2].strip()

if not(before.endswith(".csv")):
    sys.exit("Not a CSV file")

try:
    with open(before) as file:
        reader = csv.DictReader(file)
        with open(after, "w") as file1:
            writer = csv.DictWriter(file1, fieldnames = ["first","last","house"])
            writer.writeheader()
            for row in reader:
                last, first = row["name"].split(",")
                writer.writerow({"first":first.strip(),"last":last.strip(),"house":row["house"]})

except(FileNotFoundError):
    sys.exit(f"Could not read {before}")

