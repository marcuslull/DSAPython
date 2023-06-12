class MaxHeap:

    """A max heap is a complete tree that maintains the single property of a nodes children's keys are always equal
     or less than the nodes key."""

    def __init__(self):
        self.heap_array = []

    def percolate_up(self, node_index):

        while node_index > 0:
            parent_index = (node_index - 1) // 2

            if self.heap_array[node_index] <= self.heap_array[parent_index]:
                return
            else:
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[parent_index]
                self.heap_array[parent_index] = temp
                node_index = parent_index

    def percolate_down(self, node_index):
        child_index = 2 * node_index + 1
        value = self.heap_array[node_index]

        while child_index < len(self.heap_array):
            max_value = value
            max_index = -1
            i = 0
            while i < 2 and i + child_index < len(self.heap_array):
                if self.heap_array[i + child_index] > max_value:
                    max_value = self.heap_array[i + child_index]
                    max_index = i + child_index
                i += 1

            if max_value == value:
                return
            else:
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[max_index]
                self.heap_array[max_index] = temp

                node_index = max_index
                child_index = 2 * node_index + 1

    def insert(self, value):
        self.heap_array.append(value)
        self.percolate_up(len(self.heap_array) - 1)

    def remove(self):
        max_value = self.heap_array[0]
        replace_value = self.heap_array.pop()
        if len(self.heap_array) > 0:
            self.heap_array[0] = replace_value
            self.percolate_down(0)
        return max_value


















