def caesar_cipher(text, shift, mode):
    result = []
    
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    
    return ''.join(result)


def get_valid_shift():

    while True:
        try:
            shift = int(input("Enter the shift value(1-26):"))
            if shift > 0:
                return shift % 26 
            else:
                print("Shift value must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def main():
    while True:
        ## Input message and shift value from user
        message = input("Enter your message: ")
        shift = get_valid_shift()
        
        ## Encrypt the message
        encrypted_message = caesar_cipher(message, shift, 'encrypt')
        print(f"Encrypted message: {encrypted_message}")
        
        ## Prompt for decryption
        choice = input("Do you want to decrypt this message? (yes/no): ").lower()
        
        if choice == 'yes':
        ## Decrypt the message
            decrypted_message = caesar_cipher(encrypted_message, shift, 'decrypt')
            print(f"Decrypted message: {decrypted_message}")
        else:
            print("Okay, no decryption performed.")
        
        ## restart
        restart = input("Do you want to encrypt/decrypt another message? (yes/no): ").lower()
        if restart != 'yes':
            print("Exiting program. Goodbye!")
            break  

if __name__ == "__main__":
    main()
