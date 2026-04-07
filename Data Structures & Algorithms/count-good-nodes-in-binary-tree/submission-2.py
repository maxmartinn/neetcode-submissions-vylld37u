# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # problem statement
        # a node x
        # path from root to x -> node down traversal cannot be larger than x
        #                     2 1 + 1 + 1
        #              1 1           1 1
        #          1 3  0        0 1       5 1 
        # solution
        # traverse tree starting from the root node
        # store the maxValue of the traversal and see if the node is greater than the max value  
        # update res
        def dfs(node, maxVal):
            if not node:
                return 0
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            return res + dfs(node.left, maxVal) + dfs(node.right, maxVal)

        return dfs(root, float("-inf"))




