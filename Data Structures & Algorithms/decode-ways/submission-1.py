class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        if not s or s[0] == 0:
            return 0
        def dfs(i):
            if i == len(s):
                return 1
            if int(s[i]) == 0:
                return 0
            if i in memo:
                return memo[i]

            ways = dfs(i + 1)

            if 10 <= int(s[i:i+2]) <= 26:
                ways += dfs(i + 2)
            
            memo[i] = ways

            return ways
                
        return dfs(0)