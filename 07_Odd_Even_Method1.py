# Method-1:Program to check even or odd using modulus operator

# Program to check even or odd using modulus operator
number = int(input("Enter a number: "))  # Take user input and convert to integer

# If number modulo 2 equals 0, it's even; otherwise, it's odd
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")