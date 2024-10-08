t = (1, 2, 3)
# t[0] = 10  # This will raise TypeError: 'tuple' object does not support item assignment

# You can, however, create a new tuple:
t = (10,) + t[1:]
print(t) 
