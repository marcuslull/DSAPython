class Node:

    """Node class for use in some ADTs"""

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def reset_pointers(self):
        self.next = None
        self.prev = None
