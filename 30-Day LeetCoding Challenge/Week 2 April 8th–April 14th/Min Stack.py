class MinStack:

    def __init__(self):
        #initialize your data structure here.
        self.stack = []
        self.min = []
        
    def push(self, x: int) -> None:
        
        if not self.stack:
            self.min.append(x)
        elif x > self.min[-1]:
            self.min.append(self.min[-1])
        else:
            self.min.append(x)
        self.stack.append(x)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()