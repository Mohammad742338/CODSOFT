import random
import string

def generate_password():
    print("Welcome to the Password Generator!")

    # Get the desired length of the password from the user
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Please enter a positive integer for the length!")
            return
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    # Define character sets for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine all character sets
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    # Generate the password using random characters from the combined set
    password = ''.join(random.choice(all_chars) for _ in range(length))

    # Display the generated password
    print(f"\nGenerated Password: {password}")

# Run the password generator
generate_password()
