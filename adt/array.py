class Array:

    """A dynamically allocated container for storing elements"""

    def __init__(self, capacity=5):
        self.array = [None] * capacity
        self.allocation_size = capacity
        self.length = 0

    def __str__(self):
        out = "["
        for i in range(0, self.length):
            out += str(self.array[i]) + ", "
        out = out[0:-2]
        out += "]"
        return out

    def append(self, element):
        self.resize_check()
        self.array[self.length] = element
        self.length += 1

    def insert(self, element, index):
        self.resize_check()
        self.shift_right(index)
        self.array[index] = element
        self.length += 1

    def remove(self, index):
        if 0 <= index < self.length:
            self.shift_left(index)
            self.length -= 1
            self.resize_check()

    def search(self, element):
        for i in range(self.length):
            if self.array[i] == element:
                return i
        return -1

    def resize_check(self):
        if self.length >= (self.allocation_size * .7):
            self.resize()  # increase call
        elif self.length <= (self.allocation_size * .3) and self.allocation_size > 5:
            self.resize(False)  # decrease call

    def resize(self, increase=True):
        if increase:
            new_allocation_size = (self.allocation_size * 2)
        else:
            new_allocation_size = (self.allocation_size // 2)
        temp_array = [None] * new_allocation_size
        for i in range(self.length):
            temp_array[i] = self.array[i]
        self.array = temp_array
        self.allocation_size = new_allocation_size

    def shift_right(self, index):
        for i in reversed(range(index + 1, self.length + 1)):
            self.array[i] = self.array[i - 1]

    def shift_left(self, index):
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]
