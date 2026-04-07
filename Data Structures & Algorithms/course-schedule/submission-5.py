class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
        """

        clarification:

        given the prereq array where prereq[i] = [a, b]

        this indicates that course b must be taken to take course a

        [crs, pre]

        must take pre befroe crs

        naive solution:

        assume that all crses can be taken

        make and adjlist that defines what crses are avalaible and what still has courses

        if a course is contains no prereqs than the course is avalaible to be taken

        preToCrs {0 : [1], 1 : []} # {pre : crs}
        nei_count = {0 : 0, 1 : 1} {crs : nei}

        take all courses with 0 neighbors.

        then if the current course is a prereq to naother course, decrement that nei_count for that crs


        """

        preToCrs = {i : [] for i in range(numCourses)} 
        preCount = {i : 0 for i in range(numCourses)} 
        taken = 0
        visited = set()
        for crs, pre in prereq:
            preToCrs[pre].append(crs)
            preCount[crs] += 1

        q = deque(i for i in range(numCourses) if preCount[i] == 0)

        while q:
            crs = q.popleft()
            taken += 1
            neighbors = preToCrs[crs]

            for nei in preToCrs[crs]:
                preCount[nei] -= 1
                if preCount[nei] == 0:
                    q.append(nei)
        return taken == numCourses

        """
        Input: numCourses = 2, prerequisites = [[0,1]]

        Output: true


        preToCrs {0 : [1], 1 : []} # {pre : crs}
        nei_count = {0 : 0, 1 : 0} {crs : nei}
        taken_courses = 1
        visited: {}
        courses = []
        """
        
        
