class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        oneStepBack = cost[1]
        twoStepsBack = cost[0]
        for i in range(2, len(cost)):
            curr = cost[i] + min(oneStepBack, twoStepsBack)
            twoStepsBack = oneStepBack
            oneStepBack = curr
        return min(oneStepBack, twoStepsBack)

      

        return min(dp[1], dp[0])