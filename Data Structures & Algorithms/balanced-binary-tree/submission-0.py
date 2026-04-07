# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # base case
        # if not root return that it is balanced with a height of 0

        # recursive case
        # get the height of left and right and check if its balanced
        # check if left and right have a height difference of more than 1
        def dfs(root):
            if not root:
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            if left[0] and right[0]:
                if abs(left[1] - right[1]) <= 1:
                    return [True, 1 + max(left[1], right[1])]
            return [False, 1 + max(left[1], right[1])]


        return dfs(root)[0]