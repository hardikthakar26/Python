#Method:-4 Recursive function to check even or odd
#Author: HARDIK
def check_even_odd(n):
    if n == 0:
        return "even"
    elif n == 1:
        return "odd"
    else:
        return check_even_odd(n - 2)  # Subtract 2 recursively

number = int(input("Enter a number: "))  # Take user input
# Handle negative numbers by taking absolute value
result = check_even_odd(abs(number))
print(f"{number} is {result}.")