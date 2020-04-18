class Queue:

    #declearing stack
    def __init__(self):
        self.queue = list()

    #pushing values
    def push(self, data):
        self.queue.insert(0,data)

    def top(self):
        if len(self.queue)<= 0:
            return ("No elements in the stack")
        else:
            return self.queue[-1]


q = Queue()
print(q.top())
q.push("Mon")
q.push("sun")
print(q.top())
