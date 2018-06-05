class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def add_node(self, node):
        if node.value < self.value:
            if self.left is None:
                self.left = node
            else:
                self.left.add_node(node)
        elif node.value > self.value:
            if self.right is None:
                self.right = node
            else:
                self.right.add_node(node)

    def visit(self):
        if self.left is not None:
            self.left.visit()
        print(self.value)
        if self.right is not None:
            self.right.visit()

    def search(self, value):
        if self.value is value:
            return self
        elif value < self.value and self.left is not None:
            return self.left.search(value)
        elif value > self.value and self.right is not None:
            return self.right.search(value)
