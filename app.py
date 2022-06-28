import random

letters = "abcdefghijklmnopqrstuvwxyz"
symbols = "!@#$%&"
numbers = "1234567890"
password = ""

# Password Length
length_input = input("Enter password length: ")
while int(length_input) < 4 or int(length_input) > 30:
    length_input = input(
        "Password length must be greater than 3 or less than 30: ")

# Lowercase letter checker
letters_input = input("Do you want lowercase letters? Yes or no: ")
while letters_input.lower() != "yes" and letters_input.lower() != "no":
    letters_input = input("Please input yes or no: ")
# Checks if password will contain lowercase letters
if letters_input.lower() == "yes":
    password += letters

# UPPERCASE letter checker
uppercase_input = input("Do you want uppercase letters? Yes or no: ")
while uppercase_input.lower() != "yes" and uppercase_input.lower() != "no":
    uppercase_input = input("Please input yes or no: ")
# Checks if password will contain UPPERCASE letters
if uppercase_input.lower() == "yes":
    password += letters.upper()

# Numbers checker
numbers_input = input("Do you want numbers? Yes or no: ")
while numbers_input.lower() != "yes" and numbers_input.lower() != "no":
    numbers_input = input("Please input yes or no: ")
# Checks if password will contain numbers
if numbers_input.lower() == "yes":
    password += numbers

# Symbols checker
symbols_input = input("Do you want symbols? Yes or no: ")
while symbols_input.lower() != "yes" and symbols_input.lower() != "no":
    symbols_input = input("Please input yes or no: ")
# Checks if password will contain symbols
if symbols_input.lower() == "yes":
    password += symbols

generated_password = ''.join(random.choice(password) for i in range(int(length_input)))
    
print("Your generated password is: " + generated_password)