def factorial(n):
    """
    Calculate the factorial of a number.
    :param n: The number to calculate the factorial of
    :type n: int
    :return: The factorial of n
    :rtype: int
    :raises ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Accessing the docstring
print(factorial.__doc__)

# Using the function
print(factorial(5))