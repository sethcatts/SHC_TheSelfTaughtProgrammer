# - A) Add a square list to the square class that's 
#      updated with all new squares

class square():
    squareList = []
    def __init__(self, side):
        self.side = side
        self.squareList.append((self.side))
    def printSquareList(self):
        print(self.squareList)
    
sqr = square(4)
sqr = square(8)
sqr = square(16)
sqr = square(32)
sqr.printSquareList()