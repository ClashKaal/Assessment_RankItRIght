def check_leap(number):
    # Checking if the given year is leap year
    if ((number % 4 == 0) and
            (number % 400 == 0) or
            (number % 100 != 0)):
        print(number, " is a leap year")
    # Else it is not a leap year
    else:
        print(number, " is not a leap year")


# Taking an input year from user
year = int(input("Enter the number: "))
# Printing result
check_leap(year)
