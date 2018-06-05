from node import Node


class Tree:
    def __init__(self):
        self.root = None

    def add_node(self, node):
        if self.root is None:
            self.root = node
        else:
            self.root.add_node(node)

    def add_value(self, value):
        node = Node(value)
        self.add_node(node)

    def traverse(self):
        self.root.visit()

    def search(self, value):
        return self.root.search(value)
