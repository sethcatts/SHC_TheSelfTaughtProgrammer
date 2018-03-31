#Two variable calculator
# TODO: usage loop for main function
# TODO: adding, subtracting, dividing, multiplying
# TODO: set variable operators function

def calc():
    usageLoop()
    print("Calculator closed.")

def usageLoop():
    vars = setVariables()
    #ask and operate
    print("1 - Adding, 2 - Subtracting, 3 - Dividing, 4 - Multiplying")
    oper = input("Operation: ")
    if(oper = 1):
        

def setVariables():
    x = input("Set A: ")
    y = input("Set B: ")
    return [x,y]
