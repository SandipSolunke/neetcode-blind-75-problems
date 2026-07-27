class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==0:
            return -1

        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1,len(nums)):
            if curr_sum + nums[i] > 0:
                curr_sum += nums[i] 
                max_sum = max(curr_sum, max_sum)            
            else:
                curr_sum = 0
            max_sum = max(nums[i], max_sum)
            

            # print("curr sum :",curr_sum)
        return max_sum