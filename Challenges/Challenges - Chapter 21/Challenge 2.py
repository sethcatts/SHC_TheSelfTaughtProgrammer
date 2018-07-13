class Stack():
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        last = len(self.items)-1
        return self.items[last]
    def size(self):
        return len(self.items)
list = [1,2,3,4,5]
rlst = []
stack = Stack()
for i in list:
    stack.push(list[i-1])
for i in range(len(stack.items)):
    rlst.append(stack.pop())
print(rlst)
