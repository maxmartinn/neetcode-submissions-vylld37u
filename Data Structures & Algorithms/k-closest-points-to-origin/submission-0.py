class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        res = []
        for point in points:
            distance = math.sqrt((point[0] ** 2) + (point[1] ** 2))
            distances.append((distance, point[0], point[1]))
        heapq.heapify(distances)
        while len(res) != k:
            point = heapq.heappop(distances)
            res.append([point[1], point[2]])
        return res