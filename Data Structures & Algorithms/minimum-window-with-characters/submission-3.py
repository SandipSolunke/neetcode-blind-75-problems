class Solution:
    def compare_freq(self, window, target):
        for k,v in target.items():
            if window[k]<v:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        
        target = defaultdict(int)
        for ch in t:
            target[ch]+=1

        left = 0 
        curr_window = defaultdict(int)
        ans = (0, float('inf'))

        for i in range(len(s)):
            print("right ",s[i])
            curr_window[s[i]]+=1
            
            print("left ",s[left])
            print("window ",curr_window)
            print("target ",target)
            while left<i and curr_window[s[left]] > target[s[left]]:
                print("shrinking -",s[left])
                curr_window[s[left]]-=1
                left+=1

            if self.compare_freq(curr_window, target):
                print("matched ")
                if ((i-left)+1) < (ans[1]-ans[0]+1):
                    ans = (left,i)
                    print("ans updated",ans)

            # s="bdab"
            # t="ab"

        
        if ans[1]==float('inf'):
            return ""
        else:
            return s[ans[0]:ans[1]+1]

