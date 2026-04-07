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
        #                     2 1
        #               1           1 # sense two is larger than 1 (these are not good nodes)
        #           3           1       5 # 3 is larger than 1 and 2 # 5 is larger than 1 and 5

        # solution
        # traverse tree starting from the root node
        # store the maxValue of the traversal and see if the node is greater than the max value  
        # update res
        def dfs(node, maxVal):
            if not node:
                return 0
            if node.val >= maxVal:
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            return dfs(node.left, maxVal) + dfs(node.right, maxVal)

        return dfs(root, float("-inf"))




