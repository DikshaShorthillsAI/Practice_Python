x = "global"

def outer():
    x = "outer local"
    
    def inner():
        x = "inner local"
        print("inner x:", x)
    
    inner()
    print("outer x:", x)

outer()
print("global x:", x)


