class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l, r = 0, 0
        curr_window_sum = 0
        min_window_len = float('inf') 

        for r in range(len(nums)):
            curr_window_sum += nums[r]
            while curr_window_sum >= target:
                min_window_len = min(r-l+1, min_window_len)
                curr_window_sum -= nums[l]
                l+=1
            
        return 0 if min_window_len==float('inf') else min_window_len