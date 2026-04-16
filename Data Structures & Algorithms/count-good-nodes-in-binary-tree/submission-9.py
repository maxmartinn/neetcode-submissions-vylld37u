# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # at node x, if from x to root x is the largest value then it is a good node, update res by one

        # while going down the list a parameter will include largest value reached so far and current node. if the current node value is greater than largest value reached update res and make current node val the largest value
        res = 0
        def dfs(node, largest):
            nonlocal res
            if not node:
                return
            if node.val >= largest:
                res += 1
            dfs(node.left, max(node.val, largest))
            dfs(node.right, max(node.val, largest))
        dfs(root, float("-inf"))
        return res
