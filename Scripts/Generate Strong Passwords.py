import random


def generateStrongPassword():
    # Define strings containing different character sets
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "123456789"
    special_characters = "123456789!@#$%^&*()_+"

    # Concatenate all the allowed characters into a single string
    allowed_characters = lower_case + upper_case + numbers + special_characters

    # Set the desired length of the password
    number_of_characters = 16

    # Generate a random password by sampling from the allowed characters
    password = "".join(random.sample(allowed_characters, number_of_characters))

    # Print the generated password
    print(password)


generateStrongPassword()
