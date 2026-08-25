class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0 
        curr_window = [0]*26
        most_frequent = 0
        max_window_len = 0

        for i in range(len(s)):
            curr_window[ord(s[i]) - ord('A')]+=1
            most_frequent = max(most_frequent, curr_window[ord(s[i]) - ord('A')])

            if  ((i-left)+1) - most_frequent > k:
                curr_window[ord(s[left]) - ord('A')]-=1
                left+=1
            
            max_window_len = max(max_window_len, (i-left)+1)

        return max_window_len
            


