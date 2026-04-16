# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter is the height of two paths

        # each node need to return its height. current node will return the diameter and height. return the largest diameter

        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return -1
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            res = max(res, leftHeight + rightHeight + 2)
            return 1 + max(leftHeight, rightHeight)
        dfs(root)
        return res