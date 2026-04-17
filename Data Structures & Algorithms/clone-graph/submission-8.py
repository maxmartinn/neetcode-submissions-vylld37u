"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {None : None}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            oldToNew[node] = Node(node.val)
            for nei in node.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = dfs(nei)
                oldToNew[node].neighbors.append(oldToNew[nei])
            return oldToNew[node]

        dfs(node)
        return oldToNew[node]