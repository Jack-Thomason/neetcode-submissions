class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[-1] * n for _ in range(m)]

        
        def helper(i, j):
            if i == m-1 and j == n-1:
                return 1
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if i == m-1:
                dp[i][j] = helper(i, j + 1)
            elif j == n-1:
                dp[i][j] = helper(i + 1, j) 
            else:
                dp[i][j] = helper(i, j+1) + helper(i+1, j)

            return dp[i][j]

        return helper(0, 0) 
                  

            
        