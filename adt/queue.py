class Queue:

    def __init__(self, optional_max_length=-1):
        self.queue = []
        self.max_length = optional_max_length

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        out = "["
        for i in range(0, len(self)):
            out += str(self.queue[i]) + ", "
        out = out[0:-2]
        out += "]"
        return out

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        self.queue.pop(0)

    def peek(self):
        return self.queue[0]
