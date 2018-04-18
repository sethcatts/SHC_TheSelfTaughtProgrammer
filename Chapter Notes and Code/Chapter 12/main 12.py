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
