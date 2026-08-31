class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        nums_set = set(nums)
        max_count = 1

        for num in nums_set:
            curr = num
            if curr-1 not in nums_set:
                curr_count = 0
                while curr in nums_set:
                    curr_count += 1
                    curr += 1
                max_count = max(curr_count, max_count)
        
        return max_count