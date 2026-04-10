class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)

        seen = set(nums)
        max_count = 0
        for num in nums:
            if num-1 in seen:
                curr_count = 1
                while num in seen:
                    num+=1
                    curr_count+=1
                max_count = max(curr_count, max_count)
        
        return 1 if max_count==0 else max_count
