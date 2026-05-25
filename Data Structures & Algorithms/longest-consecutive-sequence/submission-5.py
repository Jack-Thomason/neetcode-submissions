class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            if num - 1 in nums:
                continue

            length = 1
            while num + length in nums:
                length += 1
            
            if length > res:
                res = length
        
        return res
