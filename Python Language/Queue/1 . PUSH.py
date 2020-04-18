class Queue:

    #declearing stack
    def __init__(self):
        self.queue = list()

    #pushing values
    def Add(self, data):
        self.queue.insert(0,data)


queue = Queue()
queue.Add("Mon")
queue.Add("Sun")
queue.Add("Kun")
