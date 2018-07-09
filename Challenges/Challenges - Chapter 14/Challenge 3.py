# - A) Write a boolean function that takes two objects and compares them
def sameObject(obj1, obj2):
    return obj1 is obj2

class objct():
    def __init__(self, name):
        self.name = name

o1 = objct('one')
o2 = objct('two')

print(sameObject(o1, o2))
print(sameObject(o1, o1))