class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        curr_window = set()
        max_window = 0

        for i in range(0,len(s)):
            while s[i] in curr_window:
                curr_window.remove(s[left])
                left += 1
            
            curr_window.add(s[i])

            max_window = max(max_window, (i-left)+1)

        return max_window