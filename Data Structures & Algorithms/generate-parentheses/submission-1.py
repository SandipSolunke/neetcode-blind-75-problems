class Solution:
    dp = {}
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        def solve(curr_string, open, close):
            if len(curr_string)==n*2:
                ans.append(curr_string)
                return
            
            if open<n:
                solve(curr_string+"(",open+1, close)
            if open>close:
                solve(curr_string+")",open, close+1)
        
        if n in Solution.dp:
            return Solution.dp[n]

        solve("",0,0)
        Solution.dp[n] = ans
        return ans