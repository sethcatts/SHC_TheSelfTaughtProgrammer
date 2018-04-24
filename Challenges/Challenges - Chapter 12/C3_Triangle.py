#Create Triangle object, create a method to return area
import math
class rightTriangle():
    def __init__(self, h, b):
        self.side_h = h
        self.side_b = b
    def return_area(self):
        return ((self.side_b * self.side_h)/2)
    def print_sides(self):
        print("Side B: ", self.side_b)
        print("Side A: ", self.side_h)
        print("Side C: ",
              math.sqrt(math.pow(self.side_b, 2) + math.pow(self.side_h, 2)))
tri = rightTriangle(12, 5)
tri.print_sides()
print(tri.return_area())
