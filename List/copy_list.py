# Using assignment 
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)  

# Using copy() method 
list3 = list1.copy()
list3.append(5)
print(list1)  
print(list3)  
