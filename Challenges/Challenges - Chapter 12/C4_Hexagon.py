#Create Hexagon object, create a method to return parimeter
class hexagon():
    def __init__(self, l):
        self.side_length = l
        self.parimeter = (l * 6)
    def get_parimeter(self):
        return self.parimeter
newHex = hexagon(4)
print(newHex.get_parimeter())
