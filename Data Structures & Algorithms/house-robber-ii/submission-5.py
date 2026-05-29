class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n == 1:
            return nums[0]
        def helper(arr):

            prev1 = 0
            prev2 = 0
            for num in arr:
                temp = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = temp

            return prev1

        
        return max(
            helper(nums[:n-1]),
            helper(nums[1:])
        )
