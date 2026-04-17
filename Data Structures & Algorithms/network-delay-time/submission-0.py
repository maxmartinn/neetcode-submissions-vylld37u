class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        dist = {} # dist from start to node

        minHeap = [(0, k)] # (weight, node)

        for u, v, t in times:
            graph[u].append((v, t))
        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in dist:
                continue
            dist[node] = time
            for nei, w in graph[node]:
                if nei in dist:
                    continue
                heapq.heappush(minHeap, (time + w, nei))
        if len(dist) < n:
            return -1
        return max(dist.values())
