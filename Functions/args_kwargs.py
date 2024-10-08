def print_args_kwargs(*args, **kwargs):
    """This function prints all positional and keyword arguments"""
    print("Positional arguments:")
    for arg in args:
        print(arg)
    
    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Using the function
print_args_kwargs(1, 2, 3, name="Diksha", age=22)

