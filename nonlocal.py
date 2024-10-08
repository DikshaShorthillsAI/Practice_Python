def outer():
    x = "outer"
    
    def inner():
        nonlocal x
        x = "inner"
        print("Inner x:", x)
    
    print("Before inner call, outer x:", x)
    inner()
    print("After inner call, outer x:", x)

outer()