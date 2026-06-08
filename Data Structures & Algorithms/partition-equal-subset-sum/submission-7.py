class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Bottom-up optimisation

        n = len(nums)
        Sum = sum(nums)

        if Sum % 2 != 0: # if sum not even then we cannot have an equal partition
            return False

        target = Sum // 2 # designate half the target

        possible = {0}

        for num in nums:
            new_possible = set(possible) # de-dupe sums
            for curr in possible: # use possible rather than new_possible as the latter changes size through iteration
                if curr + num == target:
                    return True
                
                if curr + num < target:
                    new_possible.add(curr + num)
                
            possible = new_possible
        
        return False 