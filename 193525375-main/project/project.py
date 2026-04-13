import sys
import csv
import time
import inflect

p = inflect.engine()
tym = "\nThank you for using this application." #thank you message


def main():
	confirmation = get_choice("Is this your first time using this application?") #First time user?
	name, check = check_account()

	if confirmation:
		if check:	#Account already exists.
			print("\nAn account with this name has already been created. Please login.")
			sys.exit(f"{log_in(name,check)}")
		else:
			sys.exit(f"{sign_up(name)}")

	else:
		sys.exit(f"{log_in(name,check)}")


def get_choice(message):	#Handles yes/no questions.
	while True:	#Reprompts user until a correct answer is inputted.
		print(message, end = " ")
		try:
			val = check_choice(input("Enter Yes/No:"))
		except(ValueError):
			print("Incorrect choice!")
		else:
			break
	return(bool(val))


def check_choice(choice):	#Checks if a correct answer was inputted.
	choice = choice.lower()
	choices = ["no", "n", "yes", "y"]	#List of possible choices
	if choice not in choices:
		raise ValueError

	choice = (choices.index(choice)//2)	#0 for no and 1 for yes.
	choice = True if choice == 1 else False	#Returns True for yes and False for no.

	return choice


def check_account(file_name=None):	#Checks if the account already exists.
	if file_name == None:
		file_name = input("\nWhat's your name? ")
	try:
		with open(f"{file_name}.csv") as f:	#Accounts are stored as csv files.
			return file_name, True
	except FileNotFoundError:
		return file_name, False


def sign_up(name):	#Creates account file and writes the password to it.
	print(f"\n{name} will be the name of your account. Remember it, else you'll lose access to your account!!\n")
	time.sleep(2)
	user_password = input("What should your password be? ")	#Password prompt.
	time.sleep(0.5)
	with open(f"{name}.csv", "a") as file:
		file.write(f"{user_password}\n")

	print("\nYour account has been created.")	#Account creation confirmation.
	time.sleep(0.5)

	exit = get_choice("\nDo you want to login now?")

	if exit:
		return(log_in())
	else:
		return tym


def log_in(name=None, check = False):	#Validates account name and it's password.
	if name == None:
		name, check = check_account()

	if check:
		pass
	else:
		print("Account doesn't exist. Please sign up.")
		return sign_up(name)

	login = check_password(name)	#Checks if login is successful.

	if login:
		print("Login successful.")
		return application()
	else:
		sys.exit("Try again later.")


def application():	#After successful login.
	time.sleep(1)
	print("\nLogged out.")
	return tym


def check_password(file_name):	#Validates password.
	for i in range(3):	#Accepts only 3 trials for the password.
		password = input("\nEnter your password: ")
		if password_checker(file_name, password):
			return True

		print(f"Incorrect password. You have {2-i} {p.plural_noun("attempt", 2-i)} left. Try again.")	#Displays the remaining number of trials.

	print("\nThird attempt failed.")
	return False


def password_checker(n, p):	#Opens the file and checks the password.
	with open(f"{n}.csv") as f:
			if p == f.readline().strip():
				return True
			else:
				return False


if __name__ == "__main__":
	main()
