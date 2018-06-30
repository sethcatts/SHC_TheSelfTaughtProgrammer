#Private methods will be denoted by an _underscore in python objects.
class ExampleClass:
    def _init_(self):
        self.public = "safe"
        self._unsafe = "unsafe"
    def public_method(self):
        #Clients use
        pass
    def _unsafe_method(self):
        #Clients don't use
        pass



