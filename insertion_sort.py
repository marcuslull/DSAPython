class InsertionSort:

    def __init__(self, unordered_container):
        self.unordered_container = unordered_container

    def sort(self):

        """Insertion sort progresses through an unordered container and walks back lower elements to their proper
        index"""
        for i in range(1, len(self.unordered_container)):
            pointer = i
            # print(self.unordered_container)

            while pointer > 0 and self.unordered_container[pointer] < self.unordered_container[pointer - 1]:
                temp = self.unordered_container[pointer]
                self.unordered_container[pointer] = self.unordered_container[pointer - 1]
                self.unordered_container[pointer - 1] = temp
                pointer -= 1

        return self.unordered_container
