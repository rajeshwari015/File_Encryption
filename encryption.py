from cryptography.fernet import Fernet

def generate_key():
    # Generate a random AES key
    return Fernet.generate_key()

def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()

    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    with open(output_file, 'wb') as file:
        file.write(decrypted_data)

# Example usage
input_file = input("Enter the name of the input file: ")
output_file = "encrypted.txt"  # Path to the encrypted file
decrypted_output_file = "decrypted.txt"  # Path to the decrypted file

# Generate a random key
key = generate_key()

# Encrypt the input file
encrypt_file(input_file, output_file, key)
print("File encrypted successfully!")

# Prompt for the password
password = input("Enter the password: ")

# Decrypt the encrypted file
try:
    decrypt_file(output_file, decrypted_output_file, key)
    print("File decrypted successfully!")
    # Print the decrypted content
    with open(decrypted_output_file, 'r') as file:
        print("Decrypted content:\n")
        print(file.read())
except Exception:
    print("Error: Unable to decrypt the file. The correct password is required.")
