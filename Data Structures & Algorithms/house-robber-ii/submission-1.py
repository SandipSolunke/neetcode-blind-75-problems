class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        def solve(i, curr, is_first_included):
            if i>=len(nums):
                return curr
            
            if (i, curr, is_first_included) in memo:
                return memo[(i, curr, is_first_included)]

            new_first_included = is_first_included
            if i==0:
                new_first_included = True

            if i==len(nums)-1 and is_first_included:
                new_curr =  curr
            else:
                new_curr = curr + nums[i]

            memo[(i, curr, is_first_included)] = max(
                solve(i+2, new_curr, new_first_included),
                solve(i+1, curr, is_first_included)
            )

            return memo[(i, curr, is_first_included)]

        if len(nums)==0:
            return 0

        return solve(0,0,False)