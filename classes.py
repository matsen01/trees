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


class Tree:
    def __init__(self, node):
        self.root = node
        self.leafs = self.root.find_end()

    def update_leafs(self):
        for node in self.leafs:
            if node.has_children():
                self.leafs.remove(node)
                self.leafs += node.find_end()

    def find(self, node_value):
        for node in self.leafs:
            if node.value == node_value:
                return node

    def add_node(self, node):
        parent_node = self.find(node.value)
        if node.left:
            parent_node.add_left(node.left)
        if node.right:
            parent_node.add_right(node.right)
        self.update_leafs()

    @staticmethod
    def pre_order(root):
        print(root.value)
        if root.left:
            Tree.pre_order(root.left)
        if root.right:
            Tree.pre_order(root.right)

    @staticmethod
    def post_order(root):
        if root.left:
            Tree.post_order(root.left)
        if root.right:
            Tree.post_order(root.right)
        print(root.value)
