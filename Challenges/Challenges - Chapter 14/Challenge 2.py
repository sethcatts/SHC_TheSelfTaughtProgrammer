# - A) Override the object print method for the square class so that
#      it prints length of each side of the square.
class square():
    squareList = []
    def __init__(self, side):
        self.side = side
        self.squareList.append((self.side))
    def __repr__(self):
        return("""{} by {} by {} by {} by
               """.format(self.side, self.side, self.side, self.side))
    def printSquareList(self):
        print(self.squareList)
    
sqr = square(4)
print(sqr)