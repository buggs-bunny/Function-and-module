# Python program to calculate factorial using a function

def factorial(n):
    """Return the factorial of n using a loop."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Call the function with a sample number and print the output
num = 5  # Example number
print("The factorial of", num, "is:", factorial(num))