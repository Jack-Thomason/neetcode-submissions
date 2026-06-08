class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        Sum = sum(nums)

        if Sum % 2 != 0:
            return False

        target = Sum // 2

        possible = {0}

        for num in nums:
            new_possible = set(possible)
            for curr in possible:
                if curr + num == target:
                    return True
                
                if curr + num < target:
                    new_possible.add(curr + num)
                
            possible = new_possible
        
        return False 