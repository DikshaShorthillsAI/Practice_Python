my_list = [1, 2, 3, 4, 5]
# Append 6 to the list
my_list.append(6)  # append()
print("After append(6):", my_list)
# Extend the list by adding another list [6, 7]
my_list.extend([6, 7])  # extend()
print("After extend([6, 7]):", my_list)
# Insert 10 at index 1
my_list.insert(1, 10)  # Inserts 10 at index 1
print("After insert(1, 10):", my_list)
# Remove the first occurrence of 4
my_list.remove(4)  # Removes the first occurrence of 4
print("After remove(4):", my_list)
# Remove the element at index 1 and return it
element = my_list.pop(1)  # Removes the element at index 1
print("Removed element at index 1:", element)
print("After pop(1):", my_list)
# Clear the entire list
my_list.clear()  # clear()
print("After clear():", my_list)
# Re-populate the list for further operations
my_list = [1, 2, 3, 2, 4, 5]
# Find the first occurrence of 2
index = my_list.index(2)  # Finds the first occurrence of 2
print("Index of first occurrence of 2:", index)
# Count how many times 2 appears in the list
count = my_list.count(2)  # count()
print("Count of 2 in the list:", count)
# Sort the list in ascending order
my_list.sort()  # sort()
print("After sort():", my_list)
# Sort the list in descending order
my_list.sort(reverse=True)
print("After sort(reverse=True):", my_list)
# Reverse the order of the list
my_list.reverse()  # reverse()
print("After reverse():", my_list)
# Copy the list to a new list
new_list = my_list.copy()  # copy()
print("Copied list:", new_list)
# Modifying the copied list does not affect the original list
new_list.append(4)
print("Original list after modifying the copy:", my_list)
print("Modified copy of the list:", new_list)
# Convert a tuple to a list
tuple_example = (1, 2, 3)
my_list = list(tuple_example)
print("List from tuple:", my_list)
# Convert a string to a list of characters
string_example = "Hello"
my_list = list(string_example)
print("List from string:", my_list)
