class DoublyLinkedList:

    """A node based list where each node referenced the next and previous nodes in the list"""

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node):
        node.reset_pointers()
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def prepend(self, node):
        node.reset_pointers()
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def insert_after(self, existing_node, node):
        node.reset_pointers()
        if self.head is None:
            self.head = node
            self.tail = node
        elif existing_node is self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            next_node = existing_node.next
            node.next = next_node
            node.prev = existing_node
            existing_node.next = node
            next_node.prev = node

    def remove(self, node):
        next_node = node.next
        previous_node = node.prev
        if next_node is not None:
            next_node.prev = previous_node
        if previous_node is not None:
            previous_node.next = next_node
        if node is self.head:
            self.head = next_node
        if node is self.tail:
            self.tail = previous_node

    def traverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        print()

    def reverse_traverse(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev
        print()

