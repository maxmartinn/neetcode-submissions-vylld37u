class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        childToParent = [node for node in range(n + 1)]
        componentSize = [1 for _ in range(n + 1)]

        def findRoot(node):
            while childToParent[node] != node:
                childToParent[node] = childToParent[childToParent[node]]  # point to grandparent
                node = childToParent[node]
            return node

        def union(nodeA, nodeB):
            rootA, rootB = findRoot(nodeA), findRoot(nodeB)
            if rootA == rootB:
                return False  # same component, redundant edge
            if componentSize[rootA] < componentSize[rootB]:
                rootA, rootB = rootB, rootA
            childToParent[rootB] = rootA  # attach smaller tree under larger
            componentSize[rootA] += componentSize[rootB]
            return True

        for nodeA, nodeB in edges:
            if not union(nodeA, nodeB):
                return [nodeA, nodeB]