# Creating a list of squares of numbers from 1 to 5
squares = [x ** 2 for x in range(1, 6)]
print(squares) 

# Filtering even numbers from a list
nums = [1, 2, 3, 4, 5, 6]
evens = [x for x in nums if x % 2 == 0]
print(evens) 
