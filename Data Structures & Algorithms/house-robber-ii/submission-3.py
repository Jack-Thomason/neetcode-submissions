class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) 

        if n == 1:
            return nums[0]

        def helper(i, n, memo):
            if i >= n:
                return 0
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = max(nums[i] + helper(i + 2, n, memo), helper(i + 1, n, memo))

            return memo[i]

        memo1 = [-1] * n
        memo2 = [-1] * n
        max1 = helper(0, n - 1, memo1)
        max2 = helper(1, n, memo2)
        
        return max(max1, max2)
        

