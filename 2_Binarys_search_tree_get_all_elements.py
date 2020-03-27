'''
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

The time complexity of this program is: O(n)
'''
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


class Solution:
    def __init__(self):
        self.roots_list = []

    def postorder(self, root):
        if root is None:
            return
        else:
            self.roots_list.append(root.data)
            self.postorder(root.left)
            self.postorder(root.right)

    def getAllElements(self, root1, root2):
        self.postorder(root1)
        self.postorder(root2)
        self.roots_list.sort()
        return self.roots_list


if __name__ == '__main__':
    root1 = BinarySearchTree(2)
    root1.insertnod(root1, 1)
    root1.insertnod(root1, 4)
    root2 = BinarySearchTree(2)
    root2.insertnod(root2, 1)
    root2.insertnod(root2, 5)
    sol = Solution()
    print(sol.getAllElements(root1, root2))
