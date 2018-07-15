#Hello world
print("Hello, world")
#------------------------------------------------------------------------------#
#Print "Hello, world" 100 times
for i in range(100):
    print("Hello, world!")

#Line properties of python
print("""This is a really really
really "really long line of code.""")

print\
("""This is a really really
really "really long line of code.""")

#SPACING
#Spacing is used similar to brackets in other programming languages
#Allows for distinct code blocks for the enterpreter

#DATA TYPES
#When creating variables you don't have to specify a data type...
#int
ten = 10
#string
wrd = "word"
#floating point
flt = 1.1
#boolean
test = False
#Null value
nul = None

#It is easy to change the value of a variable
print(ten)
ten = 100
print(ten)

#MATH OPERATORS
print(2+2)   #Add
print(2*2)   #Multiply
print(2-2)   #Subtract
print(2/2)   #Divid
print(2**2)  #Exponent
print(7%2)   #Modulo/remainder
print(13//8) #returns quotient

#COMPARISON OPERATORS
print(100 > 10)    #Greater than
print(100 < 10)    #Less than
print(2 >= 2)      #Greater than or equal
print(1 <= 4)      #Less than or equal to
print(6 == 9)      #Equal
print(3 != 2)      #Not equal

#LOGICAL OPERATORS
and
or
not

#CONDITIONAL STATEMENTS(if, elif, and else)
#Example
home = "America"
if home = "America":
    print("Hello, America!")
elif: home = "Japan"
    print("Hello, Japan")
elif: home = "India"
    print("Hello, India")
else:
    print("Hello, World!")
#------------------------------------------------------------------------------#
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
#------------------------------------------------------------------------------#
#- Containers & Methods -#

#---PYTHON METHODS
#Change a string to uppercase using a python Method
print("Hello".upper())
#Replace characters in a string using a Method
print("Hello".replace("o", "@"))

#---PYTHON CONTAINERS - (Store data)
#LISTS - (Ordered, All Data Types, .append(data), Mutable(editable), [])
list1 = list()
print(list1) #-> []
list2 = []
print(list2) #-> []
list3 = ["Apples", "Pears", "Peaches"]
print(list3) #-> ["Apples", "Pears", "Peaches"]
#Append list
list4 = ["Ford", "Chevy"]
list4.append("Nissan")
print(list4) #-> ["Ford", "Chevy", "Nissan"]
#Mutate
list4[1] = "Carcar"
print(list4) #-> ["Ford", "Carcar", "Nissan"]
#Pop(method)
list4.pop()
print(list4) #-> ["Ford", "Carcar"]
#Combine Lists with addition
comboList = list3 + list4
print(comboList) #-> ["Apples", "Pears", "Peaches", "Ford", "Carcar"]
#Check list for a value with 'in'
print("Ford" in comboList) #-> True
#Check for absence of a value with 'not'
print("Nissan" not in comboList) #-> True
#Get the number of items in a list
print(len(comboList)) #-> 5

#TUPLES - (Immutable, Specific order, Must always have a comma)
#Methods/Keywords - in, not in,
tuple1 = tuple()
print(tuple1) #-> ()
tuple2 = ()
print(tuple2) #-> ()
tuple3 = ("John Smith", 2000, True)
print(tuple3) #-> ("John Smith", 2000, True)
#Single Item Syntax
tuple4 = ("oneItemTuple",)
print(tuple4) #-> ("oneItemTuple",)

#DICTIONARIES - (Key-Value pair containers)
#--- Mapping, Key-Value pairs, Mutable, Not ordered, Not iteratable
#--- Keywords: ['in', 'not in'] to check for keys
dict1 = dict()
print(dict1) #-> {}
dict2 = {}
print(dict2) #-> {}
dict3 = {"Apple":"Red", "Banana":"Yellow"}
print(dict3["Apple"]) #-> "Red"
#Add a pair
dict3["Pear"] = "Brown"
#delete a pair
del dict3["Pear"]
#------------------------------------------------------------------------------#
#Triple Strings
#if a string spans more than one line you have to put it in triple quotes
""" Line one
    Line Two
    Line Three
"""

#Indexes
author = "Young"
print("Index 0 of author: " + author[0])
#Negative Indexes
print("Index -1 of author: " + author[-1])

#Strings are Immutable, create new string with mods

#Concatenation: Add strings together

#String multiplication
print("mult str" * 3) #-> "mult strmult strmult str"

#Upper and Lower built in METHODS

#Format Method
"C.J {}".format("Young") #-> "C.J Young"

"C.J {}, {} {} {}".format("Young", "was", "pretty", "smart.")
#-> "C.J Young was pretty smart"

#Split method
spl = "Hello. Yes!".split(".")
print(spl) #-> ["Hello", "Yes!"]

#Join method
jn = "abc"
result = "+".join(first_three)
print(result) #-> "a+b+c"

#Strip leading and trailing spaces
s = "         no spaces around me           "
s = s.strip()
print(s) #-> "no spaces around me"

#replace method
equ = "All goldfish go to heaven"
equ = equ.replace("o", "()")
print(equ)

#Find Indexes
print("Toaster".index("a")) #-> 3
#You need to you use exception handling if you aren't 100% sure
#that the thing you are looking for is there.

#in
"Cat" in "Cat and dog" #-> True

#Escaping characters
"Sally does \"work\""

#newline
"\n"

#Slicing
fict = ["one", "two", "three", "four", "five"]
fict = fict[0:3] #-> [first three elements]
#!There are some cool indexing tricks by leaving them blank
#------------------------------------------------------------------------------#
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

# - MODULES
#importing modules
import math
math.pow(2, 3)
import random
random.randint(0, 10)

#Aliasing MODULES
import math as m
m.pow(2, 3)

#Statistics
#this is bad form, imports should all be at the top of the doc
#but im putting the import here for easier reference.
#import statistics
nums = [1,2,3,4,5,6]
#mean
#statistics.mean(nums)
#median
#statistics.median(nums)
#mode
#statistics.mode(nums)

#keyword module
import keyword
keyword.iskeyword("for") #-> True
keyword.iskeyword("parish") #-> False

#importing written code(AAAAAAAAAaaaaaaand I have to change my file naming
#convention...)
import Chapter_8_Modules_2 as c8x
print(c8x.fun())

"""There's other notes here about stopping loose code from running when it's
imported, shouldn't be a a probem for me because I'm not slob... usually"""
#------------------------------------------------------------------------------#
#FILE ACCESS AND WRITING
import os
import csv
#Path example: /users/bob/st.txt
os.path.join("users", "bob", "st.txt")

#The open method can be called with different parameters
#
# "r" -> read only
# "w" -> write only
# "w+" -> reading and writing

#The open function returns an object called a file object

#Example
st = open("st.txt", "w")
st.write("Hi from python")
st.close()

#Example of "with" file open/close
with open("st2.txt", "w") as f:
    f.write("Hello from python")

#Reading example
with open("st2.txt", "r") as f:
    print(f.read())

#Reading to a variable for later use
myList = list()
with open("st2.txt", "r") as f:
    myList.append(f.read())
print(myList)

#CSV Files
with open("st3.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter = ',')
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])

#CSV read
with open("st3.csv", "r") as f:
    r = csv.reader(f, delimiter = ',')
    for row in r:
        print(",".join(row))

#------------------------------------------------------------------------------#
#Applying current knowledge to make a game of hangman
def hangman(word):
    wrong  = 0
    stages = ["",
              "_________          ",
              "|        |         ",
              "|      ('')        ",
              "|     / || \       ",
              "|      /  \        ",
              "|                  ",
              "|                  ",]
    rLetters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while(wrong < len(stages) - 1):
        print("\n")
        msg = "Guess a letter: "
        char = raw_input(msg)
        if char in rLetters:
            cind = rLetters.index(char)
            board[cind] = char
            rLetters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages))
        print("You lose! The word was {}.".format(word))
hangman("Power")
#------------------------------------------------------------------------------#
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
    if(oper == 1):
        print(add(vars))
    elif(oper == 2):
        print(sub(vars))
    elif(oper == 3):
        print(div(vars))
    elif(oper == 4):
        print(mul(vars))


def setVariables():
    x = input("Set A: ")
    y = input("Set B: ")
    return [x,y]
#------------------------------------------------------------------------------#
#Object Oriented Programming
"""
class [name]:
    [suites2]
"""
"""
class Orange:
    def _init_(self):
        print("Created!")
"""
class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created Orange Object")

    def rot(self, days, temp):
        self.mold = days * temp

#Instances
#or1 = Orange(10, "Dark Orange")
#print(or1.weight)
#print(or1.color)
#or1.rot(5, 85)
#print(or1.mold)


#Rectangle Object
class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l
    def area(self):
        return self.width * self.len
    def change_size(self, w, l):
        self.width = w
        self.len = l

rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())
#------------------------------------------------------------------------------#
#Private methods will be denoted by an _underscore in python objects.
class ExampleClass:
    def _init_(self):
        self.public = "safe"
        self._unsafe = "unsafe"
    def public_method(self):
        #Clients use
        pass
    def _unsafe_method(self):
        #Clients don't use
        pass
#------------------------------------------------------------------------------#
import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site
    def scrape(self):
        print("Running scrape() method")
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            #print(url)
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)

news = "https://news.yahoo.com/"

Scraper(news).scrape()

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        response = urllib.request.urlopen(self.site)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        with open("output.txt", "w") as f:
            for tag in soup.find_all('a'):
                url = tag.get('href')
                if url and 'html' in url:
                    print("\n" + url)
                    f.write(url + "\n")
#------------------------------------------------------------------------------#
class Queue():
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
class Stack():
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        last = len(self.items)-1
        return self.items[last]
    def size(self):
        return len(self.items)
#------------------------------------------------------------------------------#
