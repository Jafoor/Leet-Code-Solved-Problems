class Stack:

    #declearing stack
    def __init__(self):
        self.stack = []

    #pushing values
    def push(self, data):
        self.stack.append(data)

    #view top value 
    def peek(self):
        return self.stack[-1]


S = Stack()
S.push("Mon")
S.push("sun")
print(S.peek())
