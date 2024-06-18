import string

def check_password_strength(password):
    # Define strength categories and their criteria
    length_criteria = 8
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    
    # Assess the strength based on criteria
    if len(password) < length_criteria:
        return "Weak! Password should be at least 8 characters."
    elif not (has_uppercase and has_lowercase and has_digit and has_special):
        return "Weak! Password should include uppercase, lowercase, digits, and special characters."
    else:
        return "Strong password! Good job!"

def main():
    print("Password Strength Checker")
    print("========================")
    
    while True:
        print("Enter a password to check its strength.")
        password = input("Password: ")
        
        strength_result = check_password_strength(password)
        print(f"Password strength: {strength_result}")
        
        choice = input("Do you want to check another password? (yes/no): ").lower()
        if choice != 'yes':
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()
