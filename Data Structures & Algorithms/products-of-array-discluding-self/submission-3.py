class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1

        output = [1] * len(nums)


        for i in range(len(nums)):
            output[i] *= pre
            pre *= nums[i]
        
        for j in range(len(nums) - 1, -1, -1):
            output[j] *= post
            post *= nums[j]
        
        return output