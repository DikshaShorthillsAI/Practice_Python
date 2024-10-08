my_list = [10, 20, 30, 40, 50]

# append() - Adds an element to the end
my_list.append(60)
print(my_list)  

# insert() - Inserts an element at index 2
my_list.insert(2, 25)
print(my_list) 

# remove() - Removes the first occurrence of 30
my_list.remove(30)
print(my_list) 

# pop() - Removes and returns the last element
last_element = my_list.pop()
print(last_element)  
print(my_list)      

# sort() - Sorts the list in ascending order
unsorted_list = [3, 1, 4, 2, 5]
unsorted_list.sort()
print(unsorted_list)  

# reverse() - Reverses the list
my_list.reverse()
print(my_list) 
