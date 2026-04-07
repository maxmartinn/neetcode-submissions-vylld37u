# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # do an inorder traversal

        # get max of going left and right, just left, or just right

        # choose
        res = root.val
        def inorder(root):
            nonlocal res
            if not root:
                return 0
            left = max(0, inorder(root.left))
            right = max(0, inorder(root.right))

            max_val = root.val + left + right
            res = max(res, max_val)
            return root.val + max(left, right)
        inorder(root)
        return res