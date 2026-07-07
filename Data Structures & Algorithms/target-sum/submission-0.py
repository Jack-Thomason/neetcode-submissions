class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        n = len(nums)

        def dfs(i, curr_sum):
            if i == n:
                return 1 if curr_sum == target else 0
            
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]
            
            add = dfs(i+1, curr_sum + nums[i])
            subtract = dfs(i+1, curr_sum - nums[i])

            memo[(i, curr_sum)] = add + subtract

            return memo[(i, curr_sum)]
        
        return dfs(0, 0)

            
        
        