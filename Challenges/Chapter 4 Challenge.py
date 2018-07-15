#-1. Write a function that takes a number as an input and
#    returns that number squared
def returnInputSquared(x):
    """
    returns x^2
    :param x: int.
    """
    try:
        return x**2
    except ValueError:
        print("Invalid variable passed in")
#-2. Create a function that accepts a string as a parameter and prints it.
def printString(s):
    """
    prints s
    :param s: string
    """
    print(s)

#-3. Write a function that takes three required parameters and two optional
#    parameters
def manyParaFunction(x,y,z, a = 1, b = 1):
    """
    return the sum of x,y,z raised to a+b
    :param x,y,z,a,b: integer||float
    """
    try:
        return x+y+z**(a+b)
    except ValueError:
        print("Invalid variable passed in")
#-4. Write a program with two functions. The first should take an integer
#    as a parameter and return it divided by two. The second function should
#    take a parameter and return it multiplied by four. Save the result of the
#    first function to a variable. Call the second function using the variable
#    assigned by the first
def fOne(x):
    """
    return x divided by 2
    :param x: int.
    """
    try:
        return x/2
    except (ZeroDivisionError, ValueError):
        print("Invalid input for x")
def fTwo(x):
    """
    return x multiplied by 4
    :param x: int
    """
    try:
        return x*4
    except(ValueError):
        print("The input cannot be multiplied")

pox = fOne(6)
print(fTwo(pox))

#-5. Write a function that converts a string to a float and returns it.
def convertToFloat(s):
    """
    convert s to a floating point value and return
    :param s: string
    """
    try:
        return float(s)
    except(ValueError):
        print("The input does not convert to a floating point value.")

#-6. Add a docstring to all challenges.
#--*
#<-FUNCTION CALLS->
print(returnInputSquared(2))
printString("Test String")
print(manyParaFunction(1,0,1))
print(convertToFloat("1000"))
