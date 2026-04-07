"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = dict() # (old, new)
        if not node:
            return None
        def dfs(node):
            if node not in hashmap:
                copyNode = Node(node.val, [])
                hashmap[node] = copyNode
                for n in node.neighbors:
                    dfs(n)
        dfs(node)

        for original in hashmap:
             clone = hashmap[original]
             clone.neighbors = [hashmap[neighbor] for neighbor in original.neighbors]
        return hashmap[node]