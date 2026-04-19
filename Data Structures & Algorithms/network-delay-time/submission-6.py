class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # use a graph to create adj list with weights and nodes

        # use a min heap to store total time it took to get to that node and nodes (time, node)

        graph = {i : [] for i in range(n + 1)} # {i : (w, n)}
        for s, d, w in times:
            graph[s].append((w, d))
        dist = {} # distance from source. stores total time and node (time, n)
        minHeap = [(0, k)] # (w, m)

        while minHeap:
            w, node = heapq.heappop(minHeap)
            if node in dist:
                continue
            dist[node] = w
            for time, nei in graph[node]:
                if nei in dist:
                    continue
                heapq.heappush(minHeap, (time + w, nei))
        return max(dist.values()) if len(dist) == n else -1


        """


        Input: times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1

        graph = {0 : [], 1: [(1, 2), (4, 4)], 2 : [(1, 3)], 3 : [(1, 4)], 4 : []}
        dist = {1: 0, 2: 1, 3:2, 4: 3}
        minHeap = []
        w, node = (4, 4)

        Output: 3

        """
