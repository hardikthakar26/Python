# Method:3 Program to check even or odd using division and multiplication
#Author: HARDIK
number = int(input("Enter a number: "))  # Take user input and convert to integer

# Divide by 2, convert to int, multiply by 2, and compare to original
if (number // 2) * 2 == number:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")