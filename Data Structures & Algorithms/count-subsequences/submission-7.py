from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # top-down improved

        m, n = len(s), len(t)

        # use cache rather than memo
        @cache
        def dfs(i, j):
            if j == n:
                return 1
            if i == m:
                return 0

            if m - i < n - j:
                return 0
            
            # skip
            ways = dfs(i + 1, j)

            if s[i] == t[j]:
                ways += dfs(i + 1, j + 1)
            
            return ways
        
        return dfs(0, 0)