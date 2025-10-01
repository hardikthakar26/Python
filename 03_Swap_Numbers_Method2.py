#Method 2: Without Temporary Variable (Arithmetic Approach)
# Initialize two numbers
a = 5
b = 10

# Display original values
print("Before swapping:")
print("a =", a)
print("b =", b)

# Swap using arithmetic operations (without temporary variable)
a = a + b  # Sum of both numbers stored in 'a'
b = a - b  # Subtract 'b' from sum to get original 'a', store in 'b'
a = a - b  # Subtract new 'b' (original 'a') from sum to get original 'b'

# Display swapped values
print("\nAfter swapping (using arithmetic operations):")
print("a =", a)
print("b =", b)