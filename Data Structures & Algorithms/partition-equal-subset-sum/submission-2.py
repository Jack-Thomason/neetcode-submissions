class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        num_sum = sum(nums)

        if num_sum % 2 != 0:
            return False

        target = num_sum // 2
        memo = {}

        def helper(i, curr):
            if curr == target:
                return True
            if i >= n or curr > target:
                return False
            
            if (i, curr) in memo:
                return memo[i, curr]

            take = helper(i + 1, curr + nums[i])
            skip = helper(i + 1, curr)
            
            memo[i, curr] = take or skip
            return memo[i, curr]

        return helper(0, 0)

        