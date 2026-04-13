from datetime import date
import sys
import re
import inflect
p = inflect.engine()

def main():
    date = input("Enter your date of birth: ")

    print(sing(date))

def convert(bdate):
    today = date.today()
    birth = date.fromisoformat(bdate)
    age = today - birth
    return age.days

def sing(date):
    if not(re.search(r"^[\d]{4}-[\d]{2}-[\d]{2}$",date)):
        sys.exit(1)
    try:
        days = convert(date)
    except ValueError:
        sys.exit()
    minutes = (days * 24 * 60)
    words = p.number_to_words(minutes, andword="") + " minutes"
    return (words.capitalize())


if __name__ == "__main__":
    main()
