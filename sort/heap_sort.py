class HeapSort:

    """With each pass of heapsort over an unordered container it will remove the largest element and store it at the
     end of the container in sorted order."""

    def __init__(self, unsorted_container):
        self.unsorted_container = unsorted_container

    def max_heap_percolate_down(self, node_index, size):
        child_index = 2 * node_index + 1
        value = self.unsorted_container[node_index]

        while child_index < size:
            max_value = value
            max_index = -1
            i = 0
            while i < 2 and i + child_index < size:
                if self.unsorted_container[i + child_index] > max_value:
                    max_value = self.unsorted_container[i + child_index]
                    max_index = i + child_index
                i += 1

            if max_value == value:
                return

            temp = self.unsorted_container[node_index]
            self.unsorted_container[node_index] = self.unsorted_container[max_index]
            self.unsorted_container[max_index] = temp

            node_index = max_index
            child_index = 2 * node_index + 1

    def sort(self):
        i = len(self.unsorted_container) // 2 - 1
        while i >= 0:
            self.max_heap_percolate_down(i, len(self.unsorted_container))
            i -= 1

        i = len(self.unsorted_container) - 1
        while i > 0:
            temp = self.unsorted_container[0]
            self.unsorted_container[0] = self.unsorted_container[i]
            self.unsorted_container[i] = temp

            self.max_heap_percolate_down(0, i)
            i -= 1
