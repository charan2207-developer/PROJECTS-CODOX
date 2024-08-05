import random
import string


def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    """
    Generate a random password with the specified length and character types.

    :param length: Length of the password (default is 12).
    :param use_uppercase: Include uppercase letters (default is True).
    :param use_digits: Include digits (default is True).
    :param use_special_chars: Include special characters (default is True).
    :return: Generated password as a string.
    """
    # Define the character sets
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''

    # Combine all selected character sets
    all_chars = lower_chars + upper_chars + digits + special_chars

    if not all_chars:
        raise ValueError("No character types selected for the password.")

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password


def main():
    print("Welcome to the Password Generator!")

    # Get user input
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            raise ValueError("Password length must be greater than zero.")

        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
        use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

        # Generate and display the password
        password = generate_password(length, use_uppercase, use_digits, use_special_chars)
        print(f"Generated password: {password}")

    except ValueError as ve:
        print(f"Error: {ve}")


if __name__ == "__main__":
    main()
