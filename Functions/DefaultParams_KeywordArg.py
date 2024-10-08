def greet(name, greeting="Hello"):
    """This function greets a person with a customizable greeting"""
    return f"{greeting}, {name}!"

# Using default parameter
print(greet("Diksha"))  

# Using keyword argument
print(greet("Shashwat", greeting="Hi"))  

# Using both positional and keyword arguments
print(greet("Dilpreet", "Good morning"))  
