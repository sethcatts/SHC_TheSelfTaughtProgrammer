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

#Formate Method
"C.J {}".formate("Young") #-> "C.J Young"

"C.J {}, {} {} {}".formate("Young", "was", "pretty", "smart.")
#-> "C.J Young was pretty smart"

#Split method
spl = "Hello. Yes!".split(".")
print(spl) #-> ["Hello", "Yes!"]

#Join method
jn = "abc"
result = "+".join(first_three)
print(result) #-> "a+b+c"
