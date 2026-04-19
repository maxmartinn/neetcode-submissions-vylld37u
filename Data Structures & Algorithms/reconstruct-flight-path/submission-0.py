class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        route = []
        def dfs(node):
            while graph[node]:
                dfs(heapq.heappop(graph[node]))
            route.append(node)

        dfs("JFK")
        return route[::-1]