class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict()

        for i, num in enumerate(nums):
            val = target - num
            if val in seen:
                return [seen[val], i]
            seen[num] = i
        