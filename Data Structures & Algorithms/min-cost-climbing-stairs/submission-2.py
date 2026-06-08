class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * (len(cost) + 1)

        def helper(i, memo):
            if i < 0:
                return 0
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = cost[i] + min(helper(i - 1, memo), helper(i - 2, memo))


            return memo[i]
        
        n = len(cost)
        memo[n] = min(helper(n - 1, memo), helper(n - 2, memo))
        return memo[n]
        