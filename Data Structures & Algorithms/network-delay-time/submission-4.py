class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i : [] for i in range(n + 1)} # (i : (w, e))
 
        for s, d, w in times:
            graph[s].append((d, w))
        dist = {} # repersents distance from start to any node (i : 0)

        minHeap = [(0, k)] # (w, n)
        while minHeap:
            w, node = heapq.heappop(minHeap) # (2, 1)
            if node in dist:
                continue
            dist[node] = w # dist = {1 : 0, (2, 1)}
            for nei, d in graph[node]: # [(3, 1)]
                if nei in dist:
                    continue
                heapq.heappush(minHeap, (w + d, nei)) # heap = [(2, 1), (4, 4)]
        # graph = {0 : [], 1 : [(2, 1), (4, 4)], 2 : [(3, 1)], 3 : [(4, 1)], 4 : []}
        return max(dist.values()) if len(dist) == n else -1
                


