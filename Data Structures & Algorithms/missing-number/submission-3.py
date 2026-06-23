class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        pred_total = (n * (n+1)) // 2
        actual_total = sum(nums)

        return pred_total - actual_total
