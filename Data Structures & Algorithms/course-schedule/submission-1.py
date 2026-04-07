class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # hashmap repersenting adjacency list
        visit = set()
        preReqMap = {i: [] for i in range(numCourses)}
        for course, p in prerequisites:
            preReqMap[course].append(p)

        def dfs(c):
            if c in visit:
                return False
            if preReqMap[c] == []:
                return True
            visit.add(c)
            for pre in preReqMap[c]:
                preReqMap[c].pop()
                if not dfs(pre):
                    return False
            visit.remove(c)
            return True     

        for c in range(numCourses):
            if not dfs(c):
                return False

        
        return True
