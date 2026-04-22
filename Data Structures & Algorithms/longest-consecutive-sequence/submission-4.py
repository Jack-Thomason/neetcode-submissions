class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        in_set = set(nums)
        max_length = 0

        for num in in_set:

            if num - 1 not in in_set:
                length = 0

                while num + length in in_set:
                    length += 1
                
                if length > max_length:
                    max_length = length
        
        return max_length