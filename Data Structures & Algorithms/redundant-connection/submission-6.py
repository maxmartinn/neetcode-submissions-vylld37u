class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        # each node starts as its own root
        nodeToRoot = list(range(n + 1))
        # each component starts with size 1
        subtreeSize = [1] * (n + 1)

        def findRoot(node):
            if nodeToRoot[node] != node:
                # path compression: skip to grandparent
                nodeToRoot[node] = nodeToRoot[nodeToRoot[node]]
                node = nodeToRoot[node]
            return node

        def union(nodeA, nodeB):
            rootA, rootB = findRoot(nodeA), findRoot(nodeB)
            if rootA == rootB:
                return False  # already in same component, edge is redundant
            # attach smaller subtree under larger
            if subtreeSize[rootA] < subtreeSize[rootB]:
                rootA, rootB = rootB, rootA
            subtreeSize[rootA] += subtreeSize[rootB]  # ✅ fixed
            nodeToRoot[rootB] = rootA
            return True

        for nodeA, nodeB in edges:
            if not union(nodeA, nodeB):
                return [nodeA, nodeB]
        return []