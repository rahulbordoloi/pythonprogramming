from cryptography.fernet import Fernet

# To Generate a Symmetric (Secret) Key
key = Fernet.generate_key()
print(key)

# Encrypt the Password using the Symmetric Key
cipher_suite = Fernet(key)
ciphered_text = cipher_suite.encrypt(b"Rahul@123!")   
print(ciphered_text)

# Decrypt the Password using the Symmetric Key
unciphered_text = (cipher_suite.decrypt(ciphered_text))
print(unciphered_text)
