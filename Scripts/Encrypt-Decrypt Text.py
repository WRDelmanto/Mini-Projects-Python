from cryptography.fernet import Fernet

message = "This is a Test"

# The Key Must Have 43 Characters
seed = '123456789123456789123456789123456789123456'
key = F"b'{seed}='"

# Or Generate a Key
# key = Fernet.generate_key()

# Encrypt
fernet = Fernet(key)
encryptedMessage = fernet.encrypt(message.encode())
print("Original Message: ", message)
# print("encrypted string: ", encryptedMessage)

# Decrypt
decMessage = fernet.decrypt(encryptedMessage).decode()
print("Decrypted Message: ", decMessage)
