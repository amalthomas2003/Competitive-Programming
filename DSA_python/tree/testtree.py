class bstnode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
    
class bst:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = bstnode(value)
        else:
            self._insert_recursive(self.root, value)
        return "Inserted"
    
    def _insert_recursive(self, node, value):
        if value <= node.value:
            if node.left is None:
                node.left = bstnode(value)
                return
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = bstnode(value)
                return
            else:
                self._insert_recursive(node.right, value)
    def sort(self):
        root=self.root
        self.inorder(root)
    def inorder(self,root):
        if root is  None or root is None:
            return
        self.inorder(root.left)
        self.inorder(root.right)


tree = bst()
print(tree.insert(50))
print(tree.insert(40))
print(tree.insert(60))
print(tree.insert(30))
print(tree.insert(45))
print(tree.insert(55))
print(tree.insert(65))

tree.sort()