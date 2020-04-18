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


S = Stack()
S.push("Mon")
S.push("sun")
print(S.pop())
print(S.pop())
print(S.pop())
