my_list = [10, 20, 30, 40, 50, 60]

# Slicing from index 1 to 3 (index 3 not included)
print(my_list[1:4]) 

# Slicing from the start to index 3
print(my_list[:3])  

# Slicing from index 2 to the end
print(my_list[2:])

# Slicing with negative indexes
print(my_list[-4:-1]) 

# Slicing from index -3 to the end
print(my_list[-3:])    
# Slicing with a step of 2 (every second element)
print(my_list[::2]) 

# Slicing with a step of 3
print(my_list[::3]) 

# Changing elements in a slice
my_list[1:4] = [99, 100, 101]
print(my_list)  

# Replacing a slice with fewer elements
my_list[1:3] = [5]
print(my_list) 

# Replacing a slice with more elements
my_list[1:2] = [200, 300, 400]
print(my_list) 

# Extracting every second element
print(my_list[::2])  

# Extracting every third element
print(my_list[::3]) 
