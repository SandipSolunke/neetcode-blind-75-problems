class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = {}

        def solve(i, curr_cost):
            if i>=len(cost):
                return curr_cost
            if (i,curr_cost) in dp:
                return dp[(i,curr_cost)]

            dp[(i,curr_cost)] = min(solve(i+1, curr_cost+cost[i]), solve(i+2, curr_cost+cost[i]))

            return dp[(i,curr_cost)]
        
        return min(solve(0,0), solve(1,0))
            

            
            