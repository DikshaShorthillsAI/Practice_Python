# 1. Creating Strings
s1 = "Hello, World!"
s2 = 'Python Programming'
# 2. Accessing Characters in a String
s = "Python"
print(s[0]) 
print(s[-1])
# 3. String Slicing
s = "Programming"
print(s[0:5])  
print(s[:7])  
print(s[4:])   
# 4. String Concatenation
s1 = "Hello"
s2 = "World"
result = s1 + " " + s2
print(result) 
# 5. String Repetition
s = "Hello"
print(s * 3) 
# 6. String Length
s = "Python"
print(len(s))
# 7. Checking for Substrings
s = "Python Programming"
print("Python" in s) 
print("Java" in s)  
# 8. Changing Case
s = "hello world"
print(s.upper())     
print(s.title())      
print(s.capitalize())
# 9. Trimming Whitespace
s = "   Hello World   "
print(s.strip()) 
# 10. String Splitting and Joining
# Splitting
s = "Python is fun"
words = s.split()
print(words) 
# Joining
s = " ".join(words)
print(s) 
# 11. Finding Substrings
s = "Python is fun"
print(s.find("is")) 
print(s.count("n"))  
# 12. Replacing Substrings
s = "Hello World"
s = s.replace("World", "Python")
print(s) 
# 13. String Formatting
name = "Alice"
age = 30
# Using f-strings
s = f"My name is {name} and I am {age} years old."
print(s)
# Using format()
s = "My name is {} and I am {} years old.".format(name, age)
print(s) 
# 14. String Immutability
s = "Hello"
s = s.replace("H", "J")
print(s) 
# 15. Escape Characters
s = "Hello\nWorld"
print(s) 
# Example of tab and quotes escape characters
s = "Python\tis \"awesome\"!"
print(s)  
