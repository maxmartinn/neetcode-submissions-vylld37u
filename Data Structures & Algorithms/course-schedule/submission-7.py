class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # given a list of prerequisites as [crs, prereq]

        # naive solution:

            # use a q to contain all courses that have no prereqs remaining
            # a crs can be taken if there that course has no prereqs:

            # create a list that repersents crs as the index and the indegrees as how many prereqs are left

            # create a map of crs to prereqs, and if a crs is taken, using the list prereqs, deduct each indegree by 1
        indegree = [0 for _ in range(numCourses)]
        preToCrs = {crs: [] for crs in range(numCourses)}
        q = deque()
        for crs, pre in prerequisites:
            indegree[crs] += 1
            preToCrs[pre].append(crs)
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        while q:
            pre = q.popleft()
            for crs in preToCrs[pre]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    q.append(crs)
        return False if sum(indegree) else True
        