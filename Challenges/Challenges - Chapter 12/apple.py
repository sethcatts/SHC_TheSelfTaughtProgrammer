#Challenge 1
#Define a class Apple with four instance variables that represent apple stuff
class Apple():
    def __init__(self, t, c, w, f):
        self.type = t
        self.color = c
        self.weight = w
        self.fresh = f
    def print_self(self):
        print(self.type)
        print(self.color)
        print(self.weight)
        print(self.fresh)
goldenApple = Apple("Golden", "Gold", "Unk", "Old")
goldenApple.print_self()
