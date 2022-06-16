import sys

password = []
characters_left = -1

password_length = int(input("How long the password should be?"))

if password_length < 5:
    print("The password should be at least 5 characters long! Try again.")
    sys.exit(0)
else:
    characters_left = password_length

lowercase_letters = int(input("How many lowercase letters should the password have?"))

if lowercase_letters < 0 or lowercase_letters > characters_left:
    print("To many signs!")
    sys.exit(0)

uppercase_letters = int(input("How many uppercase letters should the password have?"))

special_characters = int(input("How many special characters should the password have?"))

digits = int(input("How many digits should the password have?"))
