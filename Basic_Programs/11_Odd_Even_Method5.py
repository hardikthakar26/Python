# Method:-5 Program to check even or odd using list indexing
#Author: HARDIK

number = int(input("Enter a number: "))  # Take user input

# Define a list where even/odd correspond to indices 0 and 1
result = ["even", "odd"]
# Use number % 2 as index to select correct string
print(f"{number} is {result[number % 2]}.")