#Python Functions

#Syntax

#def [function name]([parameters]):
#    [function definition]

#Example
def funct(x,y,z):
    return x+y+z

#Assign a variable to a function return
result = funct(1,2,3)
print(result)


#Built in functions
len("stringlength")
str(100) #-> Integer to string example
int("10000")
float(100) #-> 100.00

age = input("Input your age:")

#Required and optional parameters
def retX(x=2):
    return x

#Scope

#try-catch
#exception handling
a = input("A:")
b = input("B:")
a = int(a)
b = int(b)
try:
    print(a / b)
except (ZeroDivisionError, ValueError):
    print("b cannot be zero")

#Docstrings for functions
"""
functionality
:params x: type
"""
