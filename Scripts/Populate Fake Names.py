from faker import Faker


def generateFakeData():
    return Faker()


print(generateFakeData().name())
print(generateFakeData().address())
print(generateFakeData().text())
