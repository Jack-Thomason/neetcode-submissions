class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums) - 1
        currMax = nums[0]
        currMin = nums[0]
        maxProd = nums[0]

        for i in range(1, len(nums)):

            temp = max(nums[i], nums[i] * currMax, nums[i] * currMin)

            currMin = min(nums[i], nums[i] * currMax, nums[i] * currMin)
            currMax = temp
            
            maxProd = max(maxProd, currMax)
            
            # Update result if the new subarray sum is larger
        
        return maxProd