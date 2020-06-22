class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
    
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0] * n for _ in range(m)]
        
        dp[-1][-1] = max( 1, 1 - dungeon[-1][-1] )
        
        for j in range(n-1, 0, -1):
            dp[-1][j-1] = max( 1, dp[-1][j] - dungeon[-1][j-1] )
        
        for i in range(m-1, 0, -1):
            dp[i-1][-1] = max( 1, dp[i][-1] - dungeon[i-1][-1] )
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = min( max( 1, dp[i+1][j] - dungeon[i][j] ), max( 1, dp[i][j+1] - dungeon[i][j] ))        
        return dp[0][0]
        
        
