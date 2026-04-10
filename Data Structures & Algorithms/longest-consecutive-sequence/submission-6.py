class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)

        seen = set(nums)
        max_count = 0
        for num in nums:
            if num-1 not in seen:
                curr = num
                curr_count = 1
                while curr+1 in seen:
                    curr+=1
                    curr_count+=1
                max_count = max(curr_count, max_count)
        
        return max_count
