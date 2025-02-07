from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    print("Encrypting image...")
    # Open the image
    image = Image.open(image_path)
    # Convert image to numpy array
    image_array = np.array(image)
    # Normalize the key to be within uint8 range
    key = key % 256
    # Apply encryption (example: simple XOR with key)
    encrypted_array = image_array ^ key
    # Convert back to image
    encrypted_image = Image.fromarray(encrypted_array.astype(np.uint8))
    # Save the encrypted image
    encrypted_image.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(image_path, key, output_path):
    print("Decrypting image...")
    # Open the encrypted image
    image = Image.open(image_path)
    # Convert image to numpy array
    image_array = np.array(image)
    # Normalize the key to be within uint8 range
    key = key % 256
    # Apply decryption (same as encryption in this example)
    decrypted_array = image_array ^ key
    # Convert back to image
    decrypted_image = Image.fromarray(decrypted_array.astype(np.uint8))
    # Save the decrypted image
    decrypted_image.save(output_path)
    print("Image decrypted successfully!")

if __name__ == "__main__":
    print("Starting the program...")
    choice = input("Select an option:\n1. Encrypt an Image\n2. Decrypt an Image\nEnter your choice: ")
    if choice == '1':
        print("Encryption selected")
        image_path = input("Enter the path to the image file: ")
        key = int(input("Enter the encryption key (integer): "))
        output_path = input("Enter the output path for the encrypted image: ")
        encrypt_image(image_path, key, output_path)
    elif choice == '2':
        print("Decryption selected")
        image_path = input("Enter the path to the encrypted image file: ")
        key = int(input("Enter the decryption key (integer): "))
        output_path = input("Enter the output path for the decrypted image: ")
        decrypt_image(image_path, key, output_path)
    else:
        print("Invalid choice.")

