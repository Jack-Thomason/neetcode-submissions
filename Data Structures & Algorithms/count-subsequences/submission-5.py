class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # optimal 1-D DP

        n = len(t)

        dp = [0] * (n + 1)
        dp[0] = 1

        for char_s in s:
            for j in range(n - 1, -1, -1):
                if char_s == t[j]:
                    dp[j + 1] += dp[j]
                
        return dp[n]