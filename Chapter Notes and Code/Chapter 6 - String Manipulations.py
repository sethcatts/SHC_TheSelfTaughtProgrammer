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
fict = [0:3] #-> [first three elements]
#!There are some cool indexing tricks by leaving them blank
