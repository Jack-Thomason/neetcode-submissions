class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # top-down approach
        m, n = len(s), len(t)

        if m < n:
            return 0

        memo = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            # simple termination logic
            if j == n:
                return 1
            if i == m:
                return 0
            
            if memo[i][j] != -1:
                return memo[i][j]

            ans = 0 

            if s[i] == t[j]:
                ans = dfs(i + 1, j + 1)
            
            ans += dfs(i + 1, j)
            
            memo[i][j] = ans

            return memo[i][j]
            

        return dfs(0, 0)
