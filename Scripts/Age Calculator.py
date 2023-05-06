from datetime import date


def calculateBirth(birthYear, birthMonth, birthDay):
    # Create an object that stores the date of birth (YYYY, MM, DD)
    born = date(birthYear, birthMonth, birthDay)

    # Get the current date
    today = date.today()

    # Try to get the birthday for this year
    try:
        birthday = born.replace(year=today.year)
    except ValueError:  # Handle the case when the person was born on February 29th
        birthday = born.replace(year=today.year, month=born.month + 1, day=1)

    # Compare the birthday to the current date
    if birthday > today:
        print(today.year - born.year - 1, "years")
    else:
        print(today.year - born.year, "years")


calculateBirth(1996, 1, 5)
