count = 0

def increment():
    global count
    count += 1
    print(f"Count is now {count}")

increment() 
print(f"Final count: {count}")  
