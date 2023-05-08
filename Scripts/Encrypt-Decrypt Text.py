from cryptography.fernet import Fernet


def generateKey():
    # Generate key
    return Fernet.generate_key()


def encryptMessage(message, key=Fernet.generate_key()):
    fernet = Fernet(key)

    # Encrypt the message
    encrypted_message = fernet.encrypt(F"b{message}".encode())

    # Print the original message
    print("Original Message: ", message)

    # Print the Key
    print("Key: ", key)

    # Print the encrypted message
    print("Encrypted Message: ", encrypted_message)

    # Return the encrypted message
    return encrypted_message


def dencryptMessage(encrypted_message: bytes, key):
    fernet = Fernet(key)

    # Dencrypt the message
    decrypted_message = fernet.decrypt(encrypted_message).decode()[1:]

    # Print the decripted message
    print("Decrypted Message: ", decrypted_message)

    # Return the dencrypted message
    return decrypted_message


# If you want to generate your own key
# The Seed must have 42 characters
# seed = 'abcdefghijklmnopqrstuvwxyz0123456789012345'
# The Key must have 45 characters and start with a B(bytes) and end with ='
# key = "b" + seed + "='"

# Or let the script generate a key for you
key = generateKey()

encrypted_message = encryptMessage("This is a Test", key)
decrypted_message = dencryptMessage(encrypted_message, key)
