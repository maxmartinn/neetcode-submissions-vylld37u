class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        childToParent = [node for node in range(n + 1)]
        componentSize = [1 for _ in range(n + 1)]

        def findRoot(node):
            while childToParent[node] != node:
                childToParent[node] = childToParent[childToParent[node]]
                node = childToParent[node]
            return node
        
        def union(nodeA, nodeB):
            pA, pB = findRoot(nodeA), findRoot(nodeB)
            if pA == pB:
                return False # nodes are connected
            if componentSize[pA] < componentSize[pB]:
                pA, pB = pB, pA
            componentSize[pA] += childToParent[pB]
            childToParent[pB] = pA
            return True
        
        for nodeA, nodeB in edges:
            if not union(nodeA, nodeB):
                return [nodeA, nodeB]
        return []