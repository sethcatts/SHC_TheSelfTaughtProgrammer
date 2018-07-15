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
