class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        best = nums[0]

        for num in nums[1:]:
            current = max(current + num, num)
            best = max(best, current)
        
        return best