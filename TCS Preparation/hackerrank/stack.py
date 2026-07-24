class stack:
    def __init__(self, n):
        self.arr=[None]*n
    def push(self, data):
        self.arr[-1]=data
    def pop(self):
        return self.arr[-1]
        self.arr[-1]=None
    def peek(self):
        return self.arr[-1]

s=stack(5)
s.push(2)
s.push(5)
s.push('cpp')
print(s.peek())
print(s.pop())