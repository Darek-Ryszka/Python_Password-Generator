import sys

password = []

password_length = int(input("How long the password should be?"))

if password_length < 5:
    print("The password should be at least 5 characters long! Try again.")
    sys.exit(0)