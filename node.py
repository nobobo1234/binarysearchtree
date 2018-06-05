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
