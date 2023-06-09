class SinglyLinkedList:

    """A node based list where each node references the next node in the list."""

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
            self.tail = node

    def prepend(self, node):
        node.reset_pointers()
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def insert_after(self, existing_node, node):
        node.reset_pointers()
        if self.head is None:
            self.head = node
            self.tail = node
        elif existing_node is self.tail:
            self.tail.next = node
            self.tail = node
        else:
            node.next = existing_node.next
            existing_node.next = node

    def remove_after(self, existing_node):
        if existing_node is None and self.head is not None:
            next_node = self.head.next
            self.head = next_node
            if next_node is None:
                self.tail = None
        elif existing_node.next is not None:
            next_node = existing_node.next.next
            existing_node.next = next_node
            if next_node is None:
                self.tail = existing_node

    def traverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        print()
