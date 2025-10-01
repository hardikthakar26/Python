# Method 3: Python Tuple Swap (Most Pythonic)
#Author: HARDIK
# Initialize two numbers
a = 5
b = 10

# Display original values
print("Before swapping:")
print("a =", a)
print("b =", b)

"""
# Swap using Python's tuple unpacking feature
# Right side creates a tuple (b, a)
# Left side unpacks the tuple into variables a and b
"""
a, b = b, a

# Display swapped values
print("\nAfter swapping (using tuple unpacking):")
print("a =", a)
print("b =", b)