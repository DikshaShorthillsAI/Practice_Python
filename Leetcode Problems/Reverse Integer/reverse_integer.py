def reverse_integer(x):
    # Define the 32-bit signed integer range
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    
    # Determine the sign of x
    sign = -1 if x < 0 else 1
    x *= sign  # Work with absolute value
    
    # Reverse the digits
    reversed_x = int(str(x)[::-1])  # Reverse the string representation of x
    
    # Restore the sign
    reversed_x *= sign
    
    # Check for overflow
    if reversed_x < INT_MIN or reversed_x > INT_MAX:
        return 0
    
    return reversed_x

print(reverse_integer(123))  
print(reverse_integer(-123)) 
print(reverse_integer(120))   
print(reverse_integer(1534236469)) 
