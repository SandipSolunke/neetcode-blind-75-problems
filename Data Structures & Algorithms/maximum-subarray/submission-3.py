class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       
        curr_sum, max_sum = nums[0], nums[0]
        for i in range(1,len(nums)):
            if curr_sum <0 or curr_sum + nums[i]<=0:
                curr_sum = nums[i]
            else:
                curr_sum += nums[i]
            
            max_sum = max(curr_sum, max_sum)
        return max_sum