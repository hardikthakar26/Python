# Method:2 Program to check even or odd using bitwise AND
#Author: HARDIK
number = int(input("Enter a number: "))  # Take user input and convert to integer

# Check least significant bit: 
# number & 1 evaluates to 0 (even) or 1 (odd)
if number & 1:
    print(f"{number} is odd.")
else:
    print(f"{number} is even.")