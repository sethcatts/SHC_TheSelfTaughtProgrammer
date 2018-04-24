#Create circle object, create a method to return area
import math
class Circle():
    #Area = (pi * r)^2
    def __init__(self, r, c):
        self.radius = r
        self.circumference = c
    def diameter(self):
        return (2 * self.radius)
    def area(self):
        return math.pow((self.radius * math.pi()), 2)


circ = Circle(2, 4)
print(circ.diameter())
print(circ.area())
