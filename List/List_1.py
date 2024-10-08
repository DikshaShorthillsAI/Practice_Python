# Creating lists
my_list = [1, 2, 3, 4]
my_list = [1, "Hello", 3.14, True]
nested_list = [1, [2, 3], [4, 5]]


# Accessing elements
print(my_list[0])   
print(my_list[2])   

# Negative indexing
print(my_list[-1]) 
print(my_list[-2]) 

my_list[1] = 99  
print(my_list)    

# Basic slicing
print(my_list[1:4])   
print(my_list[:3])   
print(my_list[3:])   

# Slicing with step
print(my_list[::2])   
