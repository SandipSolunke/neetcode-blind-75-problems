class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def solve(i, curr_sum):
            if curr_sum == target and i==len(nums):
                return 1
            
            if i>=len(nums):
                return 0
            
            if (i,curr_sum) in memo:
                return memo[(i,curr_sum)]

            ans = solve(i+1, curr_sum+nums[i]) + solve(i+1, curr_sum+(-nums[i]))
            if (i, curr_sum) not in memo:
                memo[(i,curr_sum)] = ans
            return ans
        
        return solve(0, 0)