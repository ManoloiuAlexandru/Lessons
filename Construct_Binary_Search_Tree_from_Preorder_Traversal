/*Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val,and any descendant of node.right has a value > node.val.  
Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/ */

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def preorder(self, nod):
        if nod is None:
            return
        else:
            print(nod.val, end=" ")
            self.preorder(nod.left)
            self.preorder(nod.right)


class Solution:
    def bstFromPreorder(self, preorder) -> TreeNode:
        if preorder:
            root = TreeNode(preorder[0])
            root.left = self.bstFromPreorder([i for i in preorder if i < root.val])
            root.right = self.bstFromPreorder([i for i in preorder if i > root.val])
            return root
        else:
            return None


if __name__ == '__main__':
    sol = Solution()
    root = sol.bstFromPreorder([8, 5, 1, 7, 10, 12])
    root.preorder(root)
