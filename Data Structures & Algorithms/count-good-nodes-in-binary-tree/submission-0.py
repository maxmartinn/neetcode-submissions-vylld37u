# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # traverse the binary tree, passed down a value that it cannot be greater than
        res = 0
        def traverse(node, maxVal):
            nonlocal res
            if not node:
                return
            if node.val >= maxVal:
                print(node.val)
                traverse(node.left, node.val)
                traverse(node.right, node.val)
                res += 1
            else:
                traverse(node.left, maxVal)
                traverse(node.right, maxVal)
        traverse(root, float("-inf"))
        return res