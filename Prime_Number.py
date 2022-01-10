def prime_or_not(a):
    # Checking that given number is more than 1
    if a > 1:
        # Iterating over the given number with for loop
        for j in range(2, int(a / 2) + 1):

            # To check If the given number is divisible or not
            if (a % j) == 0:
                print("false")
                break

        # Else it is a prime number
        else:
            print("true")
    else:
        print("false")


# Taking an input number from the user
number = int(input("Enter the number:"))
# Printing result
prime_or_not(number)
