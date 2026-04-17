class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """

        For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
        
        in order to take course 0, course 1 needs to be taken

        which means that 0 is the coruse and 1 is the prereq

        [crs, pre]

        # create a list of prereqRemaning for each course
        # create a prereq map using prereqs mapping crs to the different prereqs
        # and populate it using the preqreqs map
        prerequisites = List[Object(crs, pre)]
        """
        res = []
        q = deque([])
        prereqsRemanining = [0 for _ in range(numCourses)]
        preToCrs = {crs : [] for crs in range(numCourses)}
        for crs, pre in prerequisites:
            prereqsRemanining[crs] += 1
            preToCrs[pre].append(crs)
        for i in range(numCourses):
            if prereqsRemanining[i] == 0:
                q.append(i)
                res.append(i)
        while q:
            curr = q.popleft()
            for crs in preToCrs[curr]:
                prereqsRemanining[crs] -= 1
                if prereqsRemanining[crs] == 0:
                    q.append(crs)
                    res.append(crs)
        return res if len(res) == numCourses else []