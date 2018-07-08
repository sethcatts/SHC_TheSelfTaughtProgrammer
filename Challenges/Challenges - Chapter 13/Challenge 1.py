# - A) Create rectangle and square classes with a method called calculate_perimeter 
#      that calculates the perimeter of the shapes they represent. 
# - B) Create rectangle and square object and call the calculate perimeter method 
#      for both of them.
class square:
    def __init__(self, s):
        self.sideLength = s
    def perimeter(self):
        return 4 * self.sideLength

sqr = square(4)
print(sqr.perimeter())
        
class rectangle:
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def perimeter(self):
        return 2 * (self.width + self.length)

rec = rectangle(12, 12)
print(rec.perimeter())