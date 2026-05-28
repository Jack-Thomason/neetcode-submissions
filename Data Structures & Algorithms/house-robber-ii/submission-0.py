class Solution:
    def rob(self, nums: List[int]) -> int:
        max1 = self.helper(nums[:-1])
        max2 = self.helper(nums[1:])
        return max(nums[0], max1, max2)

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

        


        