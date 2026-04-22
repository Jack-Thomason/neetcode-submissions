class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        i = 0
        while i < len(nums):
            current = i
            value = nums[current]
            length = 1
            while value + 1 in nums:
                length += 1
                value += 1
            if length > longest:
                longest = length

            i += 1
        return longest

        