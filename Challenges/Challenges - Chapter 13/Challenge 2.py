# - A) Define a method for the square class called change size that allows you 
#      to pass in a number that increases or decreases(if negative) the length of the
#      sides of the square.

class square:
    def __init__(self, s):
        self.sideLength = s
    def perimeter(self):
        return 4 * self.sideLength
    def change_size(self, x):
        self.sideLength = self.sideLength + x

sqr = square(4)
print(sqr.perimeter())
sqr.change_size(2)
print(sqr.perimeter())
sqr.change_size(-2)
print(sqr.perimeter())