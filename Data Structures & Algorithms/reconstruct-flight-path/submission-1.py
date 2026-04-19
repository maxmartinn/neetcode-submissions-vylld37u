class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        for s, d in tickets:
            heapq.heappush(graph[s], d)
        res = []
        def dfs(node):
            while graph[node]:
                dfs(heapq.heappop(graph[node]))
            res.append(node)
            return 
        dfs("JFK")
        return res[::-1]