class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = {0: 1}

        for num in nums:
            new_count = defaultdict(int)

            for curr_sum, ways in count.items():
                new_count[curr_sum + num] += ways
                new_count[curr_sum - num] += ways

            count = new_count
        
        return count[target]