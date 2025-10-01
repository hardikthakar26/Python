# Prompt the user for the first number
num1 = int(input("Enter the first number: "))

# Prompt the user for the second number
num2 = int(input("Enter the second number: "))

# Swap the values
num1, num2 = num2, num1

# Print the result
print(f"After swapping: First number = {num1}, Second number = {num2}")