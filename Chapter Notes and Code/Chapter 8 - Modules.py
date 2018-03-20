# - MODULES
#importing modules
import math
math.pow(2, 3)
math.randint(0, 10)

#Statistics
#this is bad form, imports should all be at the top of the doc
#but im putting the import here for easier reference.
import statistics
nums = [1,2,3,4,5,6]
#mean
statistics.mean(nums)
#median
statistics.median(nums)
#mode
statistics.mode(nums)

#keyword module
import keyword
keyword.iskeyword("for") #-> True
keyword.iskeyword("parish") #-> False

#importing written code
import Chapter 8 - Modules_2.py
print(Chapter 8 - Modules_2.py.fun())
