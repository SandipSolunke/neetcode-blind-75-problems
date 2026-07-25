class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        target = defaultdict(int)
        for ch in t:
            target[ch]+=1

        left = 0 
        curr_window = defaultdict(int)
        ans = (0, float('inf'))

        matched = 0

        for i in range(len(s)):
            curr_window[s[i]]+=1

            if s[i] in target and curr_window[s[i]]==target[s[i]]:
                matched += 1
            
            while matched == len(target):
                if (i - left + 1) < (ans[1] - ans[0] + 1):
                    ans = (left, i)
                curr_window[s[left]]-=1
                if s[left] in target and curr_window[s[left]] < target[s[left]]:
                    matched -= 1
                left += 1


        if ans[1] == float('inf'):
            return ""
        else:
            return s[ans[0]:ans[1] + 1]

