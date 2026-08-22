class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def solve(i, is_first_included):
            if i>=len(nums):
                return 0

            if i==len(nums)-1 and is_first_included:
                return 0
            
            if (i, is_first_included) in memo:
                return memo[(i, is_first_included)]

            new_first_included = is_first_included
            if i==0:
                new_first_included = True
            
            take = nums[i] + solve(i+2, new_first_included)
            skip = solve(i+1, is_first_included)

            memo[(i, is_first_included)] = max(take,skip)

            return memo[(i, is_first_included)]

        if len(nums)==0:
            return 0

        return solve(0,False)