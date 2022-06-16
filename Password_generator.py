import sys

password = []

password_length = int(input("How long the password should be?"))

if password_length < 5:
    print("The password should be at least 5 characters long! Try again.")
    sys.exit(0)

lowercase_letters = int(input("How many lowercase letters should the password have?"))

uppercase_letters = int(input("How many uppercase letters should the password have?"))

special_characters = int(input("How many special characters should the password have?"))

digits = int(input("How many digits should the password have?"))
