from tree.tree_print import pretty_tree


class Node:

    """Node class for the AVL tree"""

    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return str(self.key)

    def get_balance(self):
        left_height = -1
        if self.left is not None:
            left_height = self.left.height

        right_height = -1
        if self.right is not None:
            right_height = self.right.height

        return left_height - right_height

    def update_height(self):
        left_height = -1
        if self.left is not None:
            left_height = self.left.height

        right_height = -1
        if self.right is not None:
            right_height = self.right.height

        self.height = max(left_height, right_height) + 1

    def set_child(self, which_child, child):
        if which_child != "left" and which_child != "right":
            return False

        if which_child == "left":
            self.left = child
        else:
            self.right = child

        if child is not None:
            child.parent = self

        self.update_height()
        return True

    def replace_child(self, current_child, new_child):
        if self.left is current_child:
            return self.set_child("left", new_child)
        elif self.right is current_child:
            return self.set_child("right", new_child)

        return False


class AVLTree:

    """An AVL Tree is a balanced BST which to maintain search efficiency."""

    def __init__(self):
        self.root = None

    def __str__(self):
        return pretty_tree(self)

    def rotate_left(self, node):
        right_left_child = node.right.left
        if node.parent is not None:
            node.parent.replace_child(node, node.right)
        else:
            self.root = node.right
            self.root.parent = None

        node.right.set_child("left", node)
        node.set_child("right", right_left_child)

        return node.parent

    def rotate_right(self, node):
        left_right_child = node.left.right
        if node.parent is not None:
            node.parent.replace_child(node, node.left)
        else:
            self.root = node.left
            self.root.parent = None

        node.left.set_child("right", node)
        node.set_child("left", left_right_child)

        return node.parent

    def rebalance(self, node):
        node.update_height()

        if node.get_balance() == -2:
            if node.right.get_balance() == 1:
                self.rotate_right(node.right)

            return self.rotate_left(node)

        elif node.get_balance() == 2:
            if node.left.get_balance() == -1:
                self.rotate_left(node.left)

            return self.rotate_right(node)

        return node

    def insert(self, node):
        if self.root is None:
            self.root = node
            node.parent = None

        else:
            current_node = self.root
            while current_node is not None:
                if node.key < current_node.key:
                    if current_node.left is None:
                        current_node.left = node
                        node.parent = current_node
                        current_node = None
                    else:
                        current_node = current_node.left

                else:
                    if current_node.right is None:
                        current_node.right = node
                        node.parent = current_node
                        current_node = None
                    else:
                        current_node = current_node.right

            node = node.parent
            while node is not None:
                self.rebalance(node)
                node = node.parent

    def remove_node(self, node, USE_REMOVE_KEY_INSTEAD=0):
        if node is None:
            return False

        parent = node.parent

        if node.left is not None and node.right is not None:
            successor_node = node.right
            while successor_node.left is not None:
                successor_node = successor_node.left

            node.key = successor_node.key
            self.remove_node(successor_node)

            return True

        elif node is self.root:
            if node.left is not None:
                self.root = node.left
            else:
                self.root = node.right

            if self.root is not None:
                self.root.parent = None

            return True

        elif node.left is not None:
            parent.replace_child(node, node.left)

        else:
            parent.replace_child(node, node.right)

        node = parent
        while node is not None:
            self.rebalance(node)
            node = node.parent

        return True

    def search(self, key):
        current_node = self.root
        while current_node is not None:
            if current_node.key == key:
                return current_node
            elif current_node.key < key:
                current_node = current_node.right
            else:
                current_node = current_node.left

    def remove_key(self, key):
        node = self.search(key)
        if node is None:
            return False
        else:
            return self.remove_node(node)
