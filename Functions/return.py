def divide(a, b):
    """This function divides a by b and returns the result"""
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Using the function
print(divide(10, 2))   
print(divide(10, 0))   