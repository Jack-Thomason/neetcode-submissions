class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for k, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], k]
            else:
                seen[num] = k

