class Stack:

    """Utilizes Python's list to create a lifo container"""

    def __init__(self, optional_max_length=-1):
        self.stack = []
        self.max_length = optional_max_length

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        out = "["
        for i in range(0, len(self)):
            out += str(self.stack[i]) + ", "
        if len(out) == 1:
            return "None"
        else:
            out = out[0:-2]
            out += "]"
            return out

    def pop(self):
        self.stack.pop()

    def push(self, element):
        if len(self.stack) == self.max_length:
            return False
        self.stack.insert(len(self),element)
        return True

    def peek(self):
        return self.stack[len(self) - 1]
