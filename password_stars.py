

def main():
    """Get a password and print its length as asterisks"""
    password = get_password()
    print_asterisks(password)


def get_password():
    """Prompt the user to enter a password with a minimum length"""
    MIN_LENGTH = 8
    password = input(f"Enter a password of at least {MIN_LENGTH} characters: ")
    while len(password) < MIN_LENGTH:
        password = input(f"Enter a password of at least {MIN_LENGTH} characters: ")
    return password


def print_asterisks(password):
    """Print asterisks equal to the length of the password"""
    print('*' * len(password))


if __name__ == "__main__":
    main()
