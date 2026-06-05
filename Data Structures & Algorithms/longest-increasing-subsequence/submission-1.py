class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        ans = []
        ans.append(nums[0])

        for i in range(1, n):
            if nums[i] > ans[-1]:
                ans.append(nums[i])
            
            else:
                low = 0
                high = len(ans) - 1

                while low < high:
                    mid = low + (high - low) // 2
                    if nums[i] > ans[mid]:
                        low = mid + 1
                    else:
                        high = mid
                ans[low] = nums[i]
        return len(ans)
                    