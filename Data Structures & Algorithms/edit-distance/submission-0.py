class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

        def dfs(word1, word2, m, n, memo) -> list(int):

            if n == 0:
                return m
            if m == 0:
                return n

            if memo[m][n] != -1:
                return memo[m][n]

            
            if word1[m-1] == word2[n-1]:
                memo[m][n] = dfs(word1, word2, m-1, n-1, memo)
                return memo[m][n]
            
            memo[m][n] = 1 + min(
                dfs(word1, word2, m - 1, n - 1, memo),
                dfs(word1, word2, m, n - 1, memo),
                dfs(word1, word2, m - 1, n, memo)
            )

            return memo[m][n]

        
        return dfs(word1, word2, m, n, memo)
