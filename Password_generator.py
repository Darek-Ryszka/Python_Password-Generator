import sys

password = []
characters_left = -1


def update_characters_left(number_of_characters):
    global characters_left

    if number_of_characters < 0 or number_of_characters > characters_left:
        print("To many signs! You chose:", characters_left)
        sys.exit(0)
    else:
        characters_left -= number_of_characters
    print("Characters left: ", characters_left)


password_length = int(input("How long the password should be? "))

if password_length < 5:
    print("The password should be at least 5 characters long! Try again.")
    sys.exit(0)
else:
    characters_left = password_length

lowercase_letters = int(input("How many lowercase letters should the password have? "))
update_characters_left(lowercase_letters)

uppercase_letters = int(input("How many uppercase letters should the password have? "))
update_characters_left(uppercase_letters)

special_characters = int(input("How many special characters should the password have? "))
update_characters_left(special_characters)

digits = int(input("How many digits should the password have? "))
update_characters_left(digits)