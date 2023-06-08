class QuickSort:

    def __init__(self, unordered_container):
        self.unordered_container = unordered_container

    def partition(self, start, end):

        """The partition helper determines the pivot and does the comparing and swapping"""

        midpoint = start + (end - start) // 2
        pivot = self.unordered_container[midpoint]
        low = start
        high = end
        done = False

        while not done:
            while self.unordered_container[low] < pivot:
                low = low + 1

            while self.unordered_container[high] > pivot:
                high = high - 1

            if low >= high:
                done = True
            else:
                temp = self.unordered_container[low]
                self.unordered_container[low] = self.unordered_container[high]
                self.unordered_container[high] = temp
                low = low + 1
                high = high - 1

        return high

    def sort(self, start_index, end_index):

        """Quick sort recursively partitions the unordered container sorting each diminishing segment as it goes."""

        if end_index <= start_index:
            return

        high_index = self.partition(start_index, end_index)
        self.sort(start_index, high_index)
        self.sort(high_index + 1, end_index)
