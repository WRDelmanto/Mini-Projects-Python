from cryptography.fernet import Fernet


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


def dencryptMessage(encrypted_message: bytes, key):
    fernet = Fernet(key)

    # Dencrypt the message
    decrypted_message = fernet.decrypt(encrypted_message).decode()

    # Print the decripted message
    print("Decrypted Message: ", decrypted_message)


# The Seed must have 42 characters
seed = 'abcdefghijklmnopqrstuvwxyz0123456789012345'

# The Key must have 45 characters and start with a B(bytes) and end with ='
key = "b" + seed + "='"

encryptMessage("This is a Test", key)

encrypted_message_test = "b'gAAAAABkVUspFY-MFPL2XwQH8Mhlpr1QsHn5KNu3N9TR3IpBdzXGDwQCAkZAxNoc2isd_CIetp9xfeciFpIfnoKAEn0bCfFTuw=='"
dencryptMessage(encrypted_message_test, key)
