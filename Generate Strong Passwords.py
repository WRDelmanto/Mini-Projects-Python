import random

lowerCase = "abcdefghijklmnopqrstuvwxyz"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "123456789"
specialCharacters = "123456789!@#$%^&*()_+"

allowedCharacters = lowerCase + upperCase + numbers + specialCharacters
numberOfCharacters = 16

p = "".join(random.sample(allowedCharacters, numberOfCharacters))

print(p)
