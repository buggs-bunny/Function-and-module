import math

# Ask the user for a number as input
num = float(input("Enter a number: "))

# Calculate results using the math module
square_root = math.sqrt(num)
natural_log = math.log(num)
sine_value = math.sin(num)

# Display the results
print("Square root of", num, "is:", square_root)
print("Natural logarithm of", num, "is:", natural_log)
print("Sine of", num, "is:", sine_value)