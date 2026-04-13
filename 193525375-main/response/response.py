from validator_collection import checkers

address = input("What's your email address? ")
print("Valid") if checkers.is_email(address) else print("Invalid")
