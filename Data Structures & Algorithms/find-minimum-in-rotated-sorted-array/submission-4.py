class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = 1000

        while len(nums) > 1:
            l, r, m = 0, len(nums) - 1, len(nums) // 2
            if nums[l] > nums[m]:
                minimum = nums[m] if nums[m] < minimum else minimum
                nums = nums[l:m]
            elif nums[r] < nums[m]:
                minimum = nums[r] if nums[r] < minimum else minimum
                nums = nums[m:r]
            else:
                break
                
            



        return min(minimum, nums[0])

        
                





