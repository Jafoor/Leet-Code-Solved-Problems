class Queue:

    #declearing stack
    def __init__(self):
        self.queue = list()

    #pushing values
    def Add(self, data):
        self.queue.insert(0,data)

    #pop element
    def pop(self):
        if len(self.queue)>0:
            return self.queue.pop()
        return ("No elements in Queue!")


    #size of Queue
    def size(self):
        return len(self.queue)

queue = Queue()
queue.Add("Mon")
queue.Add("Sun")
queue.Add("Kun")
print(queue.size())
print(queue.pop())
