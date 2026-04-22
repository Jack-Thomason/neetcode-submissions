class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        subset = []
        res = []

        def print_subset(i, total):
            if total == 0:
                res.append(subset.copy())
                return
            if i == n or total < 0:
                return

            print_subset(i + 1, total) # exclude

            subset.append(nums[i])
            print_subset(i, total - nums[i])
            subset.pop()
        
        print_subset(0, target)
        return res

        