"""
NUMBER SWAPPING DEMONSTRATION PROGRAM

This program demonstrates three different methods to swap two numbers in Python:
1. Using a temporary variable
2. Using arithmetic operations (without temporary variable)
3. Using Python's tuple unpacking (most Pythonic approach)

The program also showcases the use of f-strings for formatted string output.
#Author: HARDIK
"""

def demonstrate_swapping():
    """
    Demonstrates three different methods to swap two numbers in Python.
    
    This function showcases:
    - Traditional swapping with a temporary variable
    - Arithmetic swapping without extra variables
    - Python's elegant tuple unpacking method
    - Use of f-strings for formatted output
    """
    
    # Method 1: Using a temporary variable
    print("=== Method 1: Using Temporary Variable ===")
    print("# This is the most straightforward approach that uses an intermediate variable")
    print("# to hold one value during the swap process.")
    a, b = 5, 10  # Multiple assignment in Python
    print(f"Before: a = {a}, b = {b}")  # f-string with variable interpolation
    
    # The swapping process
    temp = a  # Store the value of 'a' in a temporary variable
    a = b     # Assign the value of 'b' to 'a'
    b = temp  # Assign the original value of 'a' (from temp) to 'b'
    
    print(f"After:  a = {a}, b = {b}\n")  # Display results after swapping
    
    
    # Method 2: Using arithmetic operations (without temporary variable)
    print("=== Method 2: Using Arithmetic Operations ===")
    print("# This method uses arithmetic operations to swap values without")
    print("# requiring a temporary variable. Note: May cause overflow with very large numbers.")
    a, b = 5, 10  # Reset values
    print(f"Before: a = {a}, b = {b}")
    
    # The arithmetic swapping process
    a = a + b  # Sum both numbers and store in 'a' (a becomes 15)
    b = a - b  # Subtract original 'b' from sum to get original 'a', store in 'b' (15-10=5)
    a = a - b  # Subtract new 'b' (original 'a') from sum to get original 'b' (15-5=10)
    
    print(f"After:  a = {a}, b = {b}\n")
    
    
    # Method 3: Using tuple unpacking (Pythonic way)
    print("=== Method 3: Using Tuple Unpacking ===")
    print("# This is the most Pythonic approach. It uses tuple packing on the right")
    print("# and unpacking on the left to swap values in a single line.")
    print("# Under the hood, Python creates a temporary tuple but it's more efficient")
    print("# and readable than manual approaches.")
    a, b = 5, 10  # Reset values
    print(f"Before: a = {a}, b = {b}")
    
    # The elegant one-line swap using tuple unpacking
    a, b = b, a  # Right side creates tuple (b, a), left side unpacks it to a, b
    
    print(f"After:  a = {a}, b = {b}")


# F-STRING EXPLANATION
"""
F-STRINGS (FORMATTED STRING LITERALS)

Introduced in Python 3.6, f-strings provide a concise and readable way to embed 
expressions inside string literals.

Syntax: f"Text {expression} more text"

Key features:
1. The 'f' prefix indicates an f-string
2. Expressions inside {} are evaluated at runtime
3. Supports variables, expressions, function calls, etc.
4. Generally faster than other string formatting methods

Examples:
- Simple variables: f"Value: {x}"
- Expressions: f"Sum: {a + b}"
- Method calls: f"Name: {name.upper()}"
- Formatting: f"Price: ${price:.2f}"

Comparison with other methods:
1. f-strings (modern):      f"a = {a}, b = {b}"
2. .format() (older):       "a = {}, b = {}".format(a, b)
3. % formatting (legacy):   "a = %d, b = %d" % (a, b)
4. Concatenation (basic):   "a = " + str(a) + ", b = " + str(b)

F-strings are preferred in modern Python code for their readability and performance.
"""

# Run the demonstration if this script is executed directly
if __name__ == "__main__":
    print("NUMBER SWAPPING DEMONSTRATION")
    print("=" * 35)
    print("This program demonstrates three methods to swap two numbers in Python.\n")
    
    demonstrate_swapping()
    
    print("\n" + "=" * 35)
    print("Key Takeaways:")
    print("- Method 1 (temporary variable) is most intuitive for beginners")
    print("- Method 2 (arithmetic) avoids extra variables but may overflow")
    print("- Method 3 (tuple unpacking) is the most Pythonic and recommended")
    print("- F-strings provide clean, readable string formatting")