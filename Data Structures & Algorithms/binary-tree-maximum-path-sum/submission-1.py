# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #                   -15 (50 - 15)
        #        (10)   10                20 (40)
        #                         15      5
        #                      -5 maxPath 0

        # perform a dfs and find the largest sum starting from the root
        # either add left, right, both, or none
        res = float("-inf")
        def dfs(node):
            nonlocal res
            if not root:
                return 0
            left = 0
            right = 0
            if node.left: 
                left = max(dfs(node.left), 0)
            if node.right: 
                right = max(dfs(node.right), 0)
            allowSplit = node.val + left + right
            res = max(res, allowSplit)
            noSplit = max(node.val + left, node.val + right)
            return noSplit
        dfs(root)
        return res
