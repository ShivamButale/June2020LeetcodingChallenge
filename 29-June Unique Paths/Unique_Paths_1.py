class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(m)]for j in range(n)]
        
        for i in range(0, n):
            for j in range(0, m):
                if(i==0 or j==0):
                    dp[i][j] = 1
                else:
                    dp[i][j] = (dp[i-1][j] + dp[i][j-1])
        
        return dp[-1][-1]
