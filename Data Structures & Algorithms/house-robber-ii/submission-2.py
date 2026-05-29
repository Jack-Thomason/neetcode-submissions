class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
    
        

        def helper(i, n):
            if i >= n:
                return 0
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = max(nums[i] + helper(i + 2, n), helper(i + 1, n))

            return memo[i]


        memo = [-1] * len(nums)
        max1 = helper(0, n - 1)
        memo = [-1] * len(nums)
        max2 = helper(1, n)
        
        return max(nums[0], max1, max2)
        

