class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        seen = set()

        for num in nums:
            seen.add(num)

        i = 0
        max_count = 0
        while i<len(nums):
            if nums[i]-1 not in seen:
                curr = nums[i]+1
                curr_count = 1

                while curr in seen:
                    curr+=1
                    curr_count+=1
                
                max_count = max(max_count,curr_count)
                if max_count==len(nums):
                    return max_count
            i+=1
        return max_count
