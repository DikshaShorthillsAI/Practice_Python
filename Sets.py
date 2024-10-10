# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# Adding an element to the set
my_set.add(6)
print("Set after adding 6:", my_set)

# Removing an element from the set
my_set.remove(2)
print("Set after removing 2:", my_set)

# Sets do not allow duplicate values
dup_set = {1, 2, 2, 3}
print("Set with duplicates (duplicates are removed):", dup_set)

# Checking if an element is in the set
print("Is 3 in the set?", 3 in my_set)
