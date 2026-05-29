class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n <= 2:
            return max(nums)

        def helper(start, finish):

            prev1, prev2 = 0, 0
            for i in range(start, finish):
                prev2, prev1 = prev1, max(prev2 + nums[i], prev1)
            return prev1

        first = helper(0, n-1)
        second = helper(1, n)
        return max(
            first,
            second
        )
