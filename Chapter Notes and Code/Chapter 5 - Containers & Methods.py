#- Containers & Methods -#

#---PYTHON METHODS
#Change a string to uppercase using a python Method
print("Hello".upper())
#Replace characters in a string using a Method
print("Hello".replace("o", "@"))

#---PYTHON CONTAINERS - (Store data)
#------------------------------------------------------------------------------#

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
