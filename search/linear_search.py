class LinearSearch:

    def __init__(self, container_to_search, key_to_search_for):
        self.container_to_search = container_to_search
        self.key_to_search_for = key_to_search_for

    def position(self):

        """returns the position of the key if found or -1 if none does not work on dicts or sets"""

        for i in range(len(self.container_to_search)):
            if self.container_to_search[i] == self.key_to_search_for:
                return i
        return -1
