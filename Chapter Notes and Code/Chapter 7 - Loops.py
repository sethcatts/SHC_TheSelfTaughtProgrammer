#For-loops
def iterateName(name):
    for character in name:
        print(character)

def iterateList(list):
    for listElement in list:
        print(listElement)

def changeItemsInMutable(mutable):
    i = 0
    for item in mutable:
        new = mutable[i]
        new = new.upper()
        tv[i] = new
        i += 1
    print(mutable)

#Range-loops
def rangeLoop():
    for i in range(1,11)
        print(i)

def whileLoop():
    x = 10;
    while x > 0:
        print(x)
        x -= 1

#breakLoop needs to be tested
def breakALoop():
    for i in range(0, 100):
        print(i)
        if i > 50:
            break


#Prints all values but 3
def continueLoop():
    for i in range(1,6):
        if i == 3:
            continue
        print(i)

#You can nest loops
#Python loops are like other lang loops but harder to read...
