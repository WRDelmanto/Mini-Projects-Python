import random

allowedCharacters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+"
numberOfCharacters = 16

p = "".join(random.sample(allowedCharacters, numberOfCharacters))

print(p)
