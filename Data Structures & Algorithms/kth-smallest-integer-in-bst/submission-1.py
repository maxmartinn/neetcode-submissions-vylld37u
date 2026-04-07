# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in order traversal leads to getting values in order
        i = 0
        res = root.val
        def inorder(root):
            nonlocal i, res
            print(i)
            if not root:
                return
            inorder(root.left)
            i += 1
            if i == k:
                res = root.val
                return
            inorder(root.right)
        inorder(root)
        return res