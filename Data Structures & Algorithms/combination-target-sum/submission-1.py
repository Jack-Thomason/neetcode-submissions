class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        subset = []
        res = []

        def dfs(i, total):
            if total == 0:
                res.append(subset.copy())
                return
            if i == n or total < 0:
                return

            dfs(i + 1, total) # exclude

            subset.append(nums[i])
            dfs(i, total - nums[i])
            subset.pop()
        
        dfs(0, target)
        return res

        