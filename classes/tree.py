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
