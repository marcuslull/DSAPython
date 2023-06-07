class SelectionSort:

    def __init__(self, unordered_container):
        self.unordered_container = unordered_container

    def sort(self):

        """The selection sort algorithm uses nested for loops to sequentially iterate through an unordered collection"""

        for i in range(len(self.unordered_container) - 1):
            index_of_the_smallest = i
            # print(self.unordered_container)
            for j in range(i + 1, len(self.unordered_container)):
                if self.unordered_container[j] < self.unordered_container[index_of_the_smallest]:
                    index_of_the_smallest = j
            temp = self.unordered_container[i]
            self.unordered_container[i] = self.unordered_container[index_of_the_smallest]
            self.unordered_container[index_of_the_smallest] = temp
        return self.unordered_container
