class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_left(self, node):
        self.left = node

    def add_right(self, node):
        self.right = node

    def has_children(self):
        if self.left or self.right:
            return True

    def find_end(self):
        end = [self]
        if self.has_children():
            end.remove(self)
            if self.left:
                end += self.left.find_end()
            if self.right:
                end += self.right.find_end()
        return end

    @staticmethod
    def create_node(value, left=None, right=None):
        node = Node(value)
        if left:
            node.add_left(left)
        if right:
            node.add_right(right)
        return node