class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums) 

        left_to_right = 1
        right_to_left = 1

        maxProd = float("-inf")

        for i in range(n):

            if left_to_right == 0:
                left_to_right = 1
            if right_to_left == 0:
                right_to_left = 1

            left_to_right *= nums[i]

            j = n - i - 1

            right_to_left *= nums[j]

            maxProd = max(right_to_left, left_to_right, maxProd)

        return maxProd