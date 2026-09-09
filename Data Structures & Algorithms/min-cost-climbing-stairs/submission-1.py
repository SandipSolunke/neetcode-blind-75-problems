class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def solve(i):
            if i>=len(cost):
                return 0
            if i in dp:
                return dp[i]

            dp[i] = cost[i] + min(solve(i+1), solve(i+2))

            return dp[i]
        
        return min(solve(0), solve(1))
            

            
            