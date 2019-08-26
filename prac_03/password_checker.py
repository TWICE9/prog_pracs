"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MINIMUM_LENGTH = 4


def main():
    """Get and print password using functions."""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(min_length):
    """making sure the password meets the minimum length"""
    password = input("Enter password of at least {} characters: ".format(min_length))
    while len(password) < min_length:
        print("Invalid try again...")
        password = input("Enter password of at least {} characters: ".format(min_length))
    return password


def print_asterisks(length):
    """Prints asterisks for the length of the password"""
    print('*' * len(length))


main()
