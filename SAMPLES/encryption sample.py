from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Initialize a Fernet cipher with the key
cipher = Fernet(key)

# Encrypt data
plaintext = b"Hello, world!"
ciphertext = cipher.encrypt(plaintext)

# Decrypt data
decrypted_data = cipher.decrypt(ciphertext)
print("The encrypted data...",cipher.encrypt)
print("The decrypted text...",decrypted_data.decode())  # Output: Hello, world!
