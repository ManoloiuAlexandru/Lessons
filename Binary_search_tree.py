class BinarySearchTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insertnod(self, nod, data):
        if nod is None:
            nod = BinarySearchTree(data)
        elif data > nod.data and nod.right is None:
            nod.right = BinarySearchTree(data)
        elif data > nod.data and nod.right is not None:
            self.insertnod(nod.right, data)
        elif data < nod.data and nod.left is None:
            nod.left = BinarySearchTree(data)
        else:
            self.insertnod(nod.left, data)

    def preorder(self, nod):
        if nod is None:
            return
        else:
            print(nod.data, end=" ")
            self.preorder(nod.left)
            self.preorder(nod.right)

    def inorder(self, nod):
        if nod is None:
            return
        else:
            self.inorder(nod.left)
            print(nod.data, end=" ")
            self.inorder(nod.right)

    def postorder(self, nod):
        if nod is None:
            return
        else:
            self.postorder(nod.left)
            self.postorder(nod.right)
            print(nod.data, end=" ")