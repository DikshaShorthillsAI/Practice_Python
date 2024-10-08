# Local Scope
def my_function():
      x = 10  # Local variable
      print(x)

my_function()

#Enclosing Scope

def outer_function():
      y = 20  # Enclosing variable
      
      def inner_function():
          print(y)  # Accessing the enclosing variable
          
      inner_function()  # Output: 20

outer_function()

#Golbal Scope

z = 30  # Global variable

def another_function():
      print(z)  # Accessing global variable

another_function() 

# modifying global variable

z = 30

def modify_global():
      global z
      z += 10  # Modifies the global variable

modify_global()
print(z)  

