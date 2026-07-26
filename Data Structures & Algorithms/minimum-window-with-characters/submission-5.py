class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s=="" or t=="":
            return ""
        
        target = defaultdict(int)
        for ch in t:
            target[ch]+=1
        
        window = defaultdict(int)
        matches = 0
        left = 0

        min_len = float('inf')

        start, end = 0, 0

        for right in range(len(s)):
            ch = s[right]
            window[ch]+=1

            if ch in target and window[ch]==target[ch]:
                matches+=1
            
            while matches == len(target):
                if (right-left+1) < min_len:
                    min_len = (right-left+1)
                    start, end = left, right 

                left_ch = s[left]
                window[left_ch] -= 1

                if left_ch in target and window[left_ch] < target[left_ch]:
                    matches-=1
                left+=1
        
        return "" if min_len==float('inf') else s[start:end+1] 