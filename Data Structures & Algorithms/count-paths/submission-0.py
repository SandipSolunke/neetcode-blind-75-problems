class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        target = (m-1, n-1)

        dp = {}

        def solve(i,j):
            if (i,j) == target:
                return 1
            
            if i>=m or j>=n:
                return 0
            
            if (i,j) in dp:
                return dp[(i,j)]
                
            dp[(i,j)] = solve(i+1, j) + solve(i, j+1)

            return dp[(i,j)]
        
        return solve(0,0)