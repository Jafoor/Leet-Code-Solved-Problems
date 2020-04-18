class Stack:

    #declearing stack
    def __init__(self):
        self.stack = []

    #pushing values
    def push(self, data):
        self.stack.append(data)

    #pop element from Stack
    def pop(self):
        if len(self.stack) <= 0:
            return ("No elemennt to pop")
        else:
            return self.stack.pop()
    def top(self):
        if len(self.stack) <= 0:
            return ("No elements in the stack")
        else:
            return self.stack[-1]


S = Stack()
S.push("Mon")
S.push("sun")
print(S.top())
print(S.pop())
print(S.top())
