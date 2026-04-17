class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr, visited):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                visited[i] = True
                curr.append(nums[i])

                backtrack(curr, visited)

                curr.pop()
                visited[i] = False

        backtrack([], [False for _ in range(len(nums))]) 
        return res