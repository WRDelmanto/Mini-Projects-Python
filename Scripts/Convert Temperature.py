def celsiusToFahrenheit(celsius):
    # Convert Celsius in Fahrenheit
    fahrenheit = (celsius*1.8)+32

    print(fahrenheit)


def fahrenheitToCelsius(fahrenheit):
    # Convert Fahrenheit in Celsius
    celsius = (fahrenheit-32)/1.8

    print(celsius)


celsiusToFahrenheit(20)
fahrenheitToCelsius(68)
