class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = 1, 1

        length = len(nums)
        output = [1] * length

        for i in range(length):
            output[i] = prefix
            prefix *= nums[i]
        
        for j in range(length - 1, -1, -1):
            output[j] *= suffix
            suffix *= nums[j]

        return output