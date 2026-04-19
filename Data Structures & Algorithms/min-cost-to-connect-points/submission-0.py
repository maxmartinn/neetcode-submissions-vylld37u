class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:


        dist = {}
        minHeap = [(0, points[0][0], points[0][1])]

        while minHeap:
            w, x1, y1 = heapq.heappop(minHeap)
            if (x1, y1) in dist:
                continue
            dist[(x1, y1)] = w
            for x2, y2 in points:
                if (x2, y2) in dist:
                    continue
                m_dist = abs(x2 - x1) + abs(y2 - y1)
                heapq.heappush(minHeap, (m_dist, x2, y2))
        return sum(dist.values())