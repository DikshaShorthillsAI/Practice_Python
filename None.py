# Comprehensive Example of None Usage in Python
def greet(name=None):
    if name is None:
        print("Hello, Stranger!")
    else:
        print(f"Hello, {name}!")
# 1. Assigning None to a variable
my_var = None
print("1. my_var:", my_var)
# 2. Using None in a list
my_list = [1, 2, None, 4]
print("2. my_list:", my_list)
# 3. Using None in a dictionary
my_dict = {'name': 'Alice', 'age': None, 'city': 'New York'}
print("3. my_dict:", my_dict)
# 4. Checking if a value is None
if my_var is None:
    print("4. my_var is None")
# 5. Filling a list with None (Pre-allocating)
pre_allocated_list = [None] * 5
print("5. pre_allocated_list:", pre_allocated_list)
# 6. Using None as default parameter in functions
print("6. Function with default None parameter:")
greet()
greet("Alice")
# 7. None in conditional statements
value = None
result = "Value is None" if value is None else "Value is not None"
print("7. Conditional result:", result)
# 8. None in comparison
print("8. Comparing None:")
print("None == None:", None == None)
print("None is None:", None is None)
# 9. Returning None from a function
def function_returning_none():
    return None
result = function_returning_none()
print("9. Result of function_returning_none():", result)
# 10. None in type checking
print("10. Type of None:", type(None))
# 11. Using None as a sentinel value
def find_index(lst, target, start=None, end=None):
    start = 0 if start is None else max(start, 0)
    end = len(lst) if end is None else min(end, len(lst))
    for i in range(start, end):
        if lst[i] == target:
            return i
    return -1
numbers = [1, 2, 3, 4, 5]
print("11. Index of 3 in numbers:", find_index(numbers, 3))
print("    Index of 3 in numbers[2:]:", find_index(numbers, 3, start=2))