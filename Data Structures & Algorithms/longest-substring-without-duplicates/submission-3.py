class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left, right = 0, 0
        ans = 0
        window = set()
        while left<=right and right<len(s):
            while window and s[right] in window:
                window.remove(s[left])
                left+=1
            window.add(s[right])
            ans = max(ans, len(window))
            # print("left",s[right])
            # print("window :",window)
            # print("\n")
            right+=1
            
        
        return ans