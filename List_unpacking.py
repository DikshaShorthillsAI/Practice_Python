# 1. Basic List Unpacking
my_list = [1, 2, 3]
a, b, c = my_list
print("Basic Unpacking:")
print(a)  
print(b)  
print(c)  
print()
# 2. Ignoring Some Values with Underscore (_)
my_list = [1, 2, 3, 4]
# Only extracting the first and third values, ignoring the rest
a, _, b, _ = my_list
print("Unpacking with ignoring some values:")
print(a) 
print(b)  
print()
# 3. Unpacking with Arbitrary Length (Using * Operator)
# a. Unpacking First and Rest
my_list = [1, 2, 3, 4, 5]
first, *rest = my_list
print("Unpacking first and rest:")
print(first) 
print(rest)   
print()
# b. Unpacking First, Middle, and Last
first, *middle, last = my_list
print("Unpacking first, middle, and last:")
print(first)   
print(middle)  
print(last)   
print()
# c. Unpacking Last and Rest
*rest, last = my_list
print("Unpacking last and rest:")
print(rest)  
print(last) 
print()
# 4. Unpacking for Function Arguments
def add(a, b, c):
    return a + b + c

my_list = [1, 2, 3]
# Unpacking the list into individual arguments
result = add(*my_list)
print("Unpacking for function arguments:")
print(result)  
print()
# 5. Unpacking in Loops
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
print("Unpacking in loops:")
# Unpacking the tuples in the loop
for num, word in pairs:
    print(f'{num} is {word}')
print()
# 6. Unpacking with zip()
numbers = [1, 2, 3]
words = ['one', 'two', 'three']
print("Unpacking with zip:")
for num, word in zip(numbers, words):
    print(f'{num} is {word}')
print()
# 7. Unpacking Nested Lists
nested_list = [[1, 2], [3, 4], [5, 6]]
print("Unpacking nested lists:")
for a, b in nested_list:
    print(a, b)
print()
# 8. Using * to Flatten a List
list1 = [1, 2]
list2 = [3, 4]
# Using * to flatten them into one list
combined = [*list1, *list2]
print("Flattening two lists:")
print(combined)  
print()
# 9. Unpacking in List Comprehensions
pairs = [(1, 2), (3, 4), (5, 6)]
sums = [a + b for a, b in pairs]
print("Unpacking in list comprehensions:")
print(sums) 
