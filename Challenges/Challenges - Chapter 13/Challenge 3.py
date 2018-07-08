# - A) Create a class called shape. Define a method in it called what_am_i that prints 
#      "I'm a shape" when called. 
# - B) Change the square and rectangle classes to inherit from shape,
#      call the method on instances of the two shapes.

class shape():
    def what_am_i(self):
        print("I am a shape")

class square(shape):
    def __init__(self, s):
        self.sideLength = s
    def perimeter(self):
        return 4 * self.sideLength

class rectangle(shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l
    def perimeter(self):
        return 2 * (self.width + self.length)

sqr = square(4)
print(sqr.perimeter())
print(sqr.what_am_i())

rec = rectangle(12, 12)
print(rec.perimeter())
print(sqr.what_am_i())