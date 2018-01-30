#Number to be used in most funcion cal
number = 15

#-1. Print 3 different strings
def print3Strings(x):
    print("String1")
    print("String2")
    print("String3")

#-2. Write a program that prints a message if a variable is less than 10, and
#    a different message if the variable is greater than or equal to 10.
def tenOrGreater(num):
    if num >= 10:
        print("The number is equal to or greater than 10")
    else:
        print("The input number is less than 10")

#-3. Write a program that prints a message if a variable is less than or equal
#    to 10, and another if the variable is greater than 10 but less than or
#    equal to 25, and another if the variable is greater than 25
def rangeOfInput(num):
    if num <= 10:
        print("Less than or equal to 10")
    elif num > 10 and num <= 25:
        print("Between 11 and 26")
    else:
        print("Greater than 25")

#-4. Create a program that divides 2 variables and returns the remainder
def retRemainder(x, y):
    return x % y
#-5. Create a program that takes two variables divides them and returns quotient
def retQuotient(x, y):
    return x/y
#-6. Write a program with a variable "age" assigned to an integer that prints
#    different strings depending on the value of the integer
def ageProps(age):
    if age < 2:
        print("Baby")
    elif age <= 12 and age > 2:
        print("Child")
    elif age < 20 and age > 12:
        print("Teenager")
    else:
        print("Adult")

#--FUNCTION CALLS--
#print3Strings(1)
#tenOrGreater(number)
#rangeOfInput(number)
#print(retRemainder(5,2))
#print(retQuotient(9,3))
#ageProps(10)
