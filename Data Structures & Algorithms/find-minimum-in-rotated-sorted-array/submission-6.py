class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        l, r = 0, len(nums) - 1

        while l < r:
            m = (r + l) // 2
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m
              
        return nums[l]

        
                





