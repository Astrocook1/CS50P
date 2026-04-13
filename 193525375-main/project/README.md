# ACCOUNT MANAGEMENT SYSTEM

## Project Description
This project implements an account management system. It simulates account creation and log-in processes with account name and password validations.

## File Structure
### project.py
This is the main and only file of the program. It contains the functions of the account management program that handles all the processes from account creation to user validation. The various functions are briefly described below.

- main(): This is the main function of the system. The function asks the user, with the get_choice() function, if he/she is a first time user -in order to proceed with the sign-up or log-in process. It validates if the user made the correct choice by prompting the user for a name and calling the check_account() function to check if an account with that name has already been created before proceeding with the appropriate processes and exiting the program when done with a thank you message to the user.

- get_choice(message): This function handles yes or no questions by prompting the user for an answer to the message (question) passed to it. It continues reprompting the user until a correct answer is inputted. It validates the answer with the check_choice() function by passing the choice in lowercase. 

- check_choice(choice): This function checks if the choice passed to it was within yes,y,no or n.
 
- check_account(file_name=None): This function prompts the user for a name if none is passed to it and checks if an account with that name has already been created.
 
- sign_up(name): The sign_up() function creates an account with the user's name and prompts the user for a password to the account. It saves it in a csv file and completes the sign-up process.
 
- log_in(name=None, check=False): The log_in() function prompts for the user for the account name if necessary and validates it with the password stored in the account's csv file with the check_password() function. If successful, it logs in the user into the application. If the account name doesn't exist, it prompts the user to sign-up.
 
- application(): This function simulates a successful log-in process by keeping the user logged in for a short while and logging the user out after the time has elapsed.
 
- check_password(file_name): This function prompts the user for the correct password only thrice by validating it with the password_checker() function. It passes the account's name (file_name) and the password inputted by the user to the function. 
 
- password_checker(n,p): This function checks if the password passed to it (p) is the correct password stored in the account's name (n) csv file.

### CS50.csv
This is an account created with the account system and used with to simulate other functions in the system. It is also used in the test_project.py program.
  
### test_project.py
This tests the check_choice(), check_account() and check_password() functions by ensuring it gives the correct outputs. Some functions in this program makes use of the CS50.csv account created by project.py. 

### requirements.txt
This lists the pip installable libraries used in the project.


## Design Choices
1. Intially, a class was chosen to implement the yes/no choices as objects but it was later replaced by the get_choice() and check_choice() functions. This was to cancel some errors because the result of the class had to be explicitly converted to boolean by the function that creates the object in order to know if a correct choice had been inputted.

2. The accounts were chosen to be stored in csv files in order to allow for future improvements like storing log times or including passkeys or passcodes for user validation. Txt files cannot efficiently handle these upgrades when compared to txt files.

3. Only the main() and log_in() functions can exit the program. The log_in() does that only when the user fails to enter the correct password after 3 trials. Else, the functions return to the main() function which then exits the program by displaying the thank you message. I made this choice to ensure that only the main function displays the thank you message.
 
#### Video Demo: https://youtu.be/F5AfsWbEDGk?si=7xtlxctpnHC5_69a
> This is a short video that shows the application in operation. 
