# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # the lowest common ancestor is when p and q fall under the same node
        # the lowest common ancestor occurs when curr is greater than p and curr is less than q

        if p.val > q.val:
            p, q = q, p
        curr = root
        while curr:
            while curr.left and p.val < curr.val and q.val < curr.val:
                curr = curr.left
            while curr.right and p.val > curr.val and q.val > curr.val:
                curr = curr.right
            if p.val <= curr.val and q.val >= curr.val:
                return curr
        return root
