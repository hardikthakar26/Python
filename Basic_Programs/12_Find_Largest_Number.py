"""
Program: Find Largest of Three Numbers
Description: This program takes three numbers as input from the user and finds the largest among them.
Author: HARDIK
Date: 2024
"""

def find_largest_of_three():
    """
    This function finds the largest of three numbers entered by the user.
    It uses conditional statements to compare the numbers and determine the largest one.
    """
    
    # Display program purpose to user
    print("=== Largest Number Finder ===")
    print("This program will find the largest of three numbers you enter.")
    print()
    
    # INPUT PHASE: Get three numbers from user
    # We use float() to handle both integers and decimal numbers
    # input() function gets user input as string, float() converts it to number
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    
    # PROCESSING PHASE: Compare numbers to find largest
    # Logic: We compare each number with the other two to find which is largest
    
    # Check if first number is greater than or equal to both second and third
    if num1 >= num2 and num1 >= num3:
        # If condition is True, num1 is the largest
        largest = num1
        # Store which number was largest for display
        position = "first"
    
    # If first condition fails, check if second number is largest
    elif num2 >= num1 and num2 >= num3:
        # If condition is True, num2 is the largest
        largest = num2
        position = "second"
    
    # If both above conditions fail, third number must be largest
    else:
        # No need to check condition since it's the only possibility left
        largest = num3
        position = "third"
    
    # OUTPUT PHASE: Display the result to user
    print()
    print("=" * 40)  # Print separator line
    print("RESULT:")
    print(f"You entered: {num1}, {num2}, {num3}")
    print(f"The largest number is: {largest}")
    print(f"This was the {position} number you entered.")
    print("=" * 40)

# Alternative method using max() function - commented out for reference
"""
def find_largest_simple():
    # This method uses Python's built-in max() function
    # It's simpler but doesn't show the comparison logic
    
    print("=== Largest Number Finder (Simple Version) ===")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    
    # max() function returns the largest of the given arguments
    largest = max(num1, num2, num3)
    
    print(f"The largest number is: {largest}")
"""

# Main execution block
# This code runs when the script is executed directly
if __name__ == "__main__":
    # Call the function to execute the program
    find_largest_of_three()
    
    # Optional: Ask user if they want to run again
    while True:
        print()
        run_again = input("Do you want to find largest of another set of numbers? (yes/no): ").lower()
        if run_again in ['yes', 'y']:
            find_largest_of_three()
        elif run_again in ['no', 'n']:
            print("Thank you for using the program. Goodbye!")
            break
        else:
            print("Please enter 'yes' or 'no'.")