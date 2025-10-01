# Method 1: Using a Temporary Variable

# Initialize two numbers
a = 5
b = 10

# Display original values
print("Before swapping:")
print("a =", a)
print("b =", b)

# Swap using a temporary variable
temp = a  # Store value of 'a' in temporary variable
a = b     # Assign value of 'b' to 'a'
b = temp  # Assign original value of 'a' (from temp) to 'b'

# Display swapped values
print("\nAfter swapping (using temporary variable):")
print("a =", a)
print("b =", b)