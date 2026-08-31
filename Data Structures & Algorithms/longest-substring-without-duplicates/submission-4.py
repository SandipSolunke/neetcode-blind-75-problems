class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,0
        curr_window = set()
        ans = 0
        for r in range(len(s)):

            while s[r] in curr_window:
                curr_window.remove(s[l])
                l+=1
            curr_window.add(s[r])

            ans = max(ans, len(curr_window))
        
        return ans