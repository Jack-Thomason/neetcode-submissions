class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        num_sum = sum(nums)

        if num_sum % 2 != 0:
            return False

        half = num_sum // 2
        curr = 0

        def helper(i, curr):
            if i >= n:
                return False
            if curr == half:
                return True
            if curr > half:
                return False
            
            
            
            if helper(i + 1, curr + nums[i]):
                return True
            elif helper(i + 1, curr):
                return True
            else:
                return False
        
        return helper(0, curr)

        