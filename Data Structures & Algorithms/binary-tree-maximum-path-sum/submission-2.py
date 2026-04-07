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
        res = [root.val]
        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            res[0] = max(res[0], node.val + left + right)
            return node.val + max(left, right)
        dfs(root)
        return res[0]
