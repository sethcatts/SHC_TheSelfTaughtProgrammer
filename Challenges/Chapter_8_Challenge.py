import math
import Chapter_8_Module as c8m
#-1 Call a different functions from a built in method
def c1(x):
    return math.fabs(x)
#-2 Create a module named cubed with a function that takes a number and returns
#   the cube of the number, import and call it in another module.
def filler():
    return False
    #See function calls below


#Function calls
print(c1(-5))
print(c8m.cube(3))
