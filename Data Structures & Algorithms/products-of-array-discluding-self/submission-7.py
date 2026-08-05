class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1

        length = len(nums)
        output = [1] * length

        #prefix calculation
        for i in range(length):
            output[i] = prefix #output[i] = >nums[:i]< * nums[i+1:]
            prefix *= nums[i] # prefix[i] = product(nums[:i])

        #suffix calculation
        for i in range(length - 1, -1, -1):
            output[i] *= suffix # output[i] = nums[:i] * >nums[i+1:]<
            suffix *= nums[i]
        
        return output