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
