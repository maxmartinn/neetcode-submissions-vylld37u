# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # going from the bottom return maximum of going down one of the paths
        res = float("-inf")
        if not root:
            return 0
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            max_val = max(node.val, left + node.val, right + node.val, node.val + left + right)
            res = max(res, max_val)
            return max(node.val, node.val + max(left, right))

        dfs(root)
        return res