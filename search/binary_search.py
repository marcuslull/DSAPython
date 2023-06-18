class BinarySearch:
    """Binary Search Class - Worst case time complexity: O(logN)"""

    def __init__(self, container_to_search, key_to_search_for):
        self.container_to_search = container_to_search
        self.key_to_search_for = key_to_search_for

    def position(self):

        """returns the position of the key if found or -1 if none does not work on unordered collections"""

        low_pointer = 0
        high_pointer = len(self.container_to_search) - 1

        while high_pointer >= low_pointer:
            mid_pointer = (high_pointer + low_pointer) // 2
            if self.container_to_search[mid_pointer] < self.key_to_search_for:  # search the upper half
                low_pointer = mid_pointer + 1
            elif self.container_to_search[mid_pointer] > self.key_to_search_for:  # search the lower half
                high_pointer = mid_pointer - 1
            else:
                return mid_pointer
        return -1  # key not found
