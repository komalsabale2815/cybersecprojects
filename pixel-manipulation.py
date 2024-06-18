from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size
    
    # Convert image to numpy array for fast pixel manipulation
    img_array = np.array(img)
    
    # Apply encryption (e.g., XOR operation)
    encrypted_img_array = img_array ^ key
    
    # Create encrypted image from numpy array
    encrypted_img = Image.fromarray(encrypted_img_array)

    # Save encrypted image
    encrypted_img.save('encrypted_image.png')
    
    print("Image encrypted successfully. Saved as 'encrypted_image.png'")

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    
    # Convert image to numpy array for fast pixel manipulation
    encrypted_img_array = np.array(encrypted_img)
    
    # Apply decryption (same operation as encryption since XOR is its own inverse)
    decrypted_img_array = encrypted_img_array ^ key
    
    # Create decrypted image from numpy array
    decrypted_img = Image.fromarray(decrypted_img_array)
    
    # Save decrypted image
    decrypted_img.save('decrypted_image.png')
    
    print("Image decrypted successfully. Saved as 'decrypted_image.png'")

def main():
    image_path = input("Enter the path of the image file to encrypt: ")
    key = int(input("Enter an integer key for encryption: "))
    
    # Encrypt the image
    encrypt_image(image_path, key)
    
    # Decrypt the image
    encrypted_image_path = 'encrypted_image.png'  # Assuming it was saved as encrypted_image.png
    decrypt_image(encrypted_image_path, key)

if __name__ == "__main__":
    main()
