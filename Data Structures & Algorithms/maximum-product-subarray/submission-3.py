class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # Approach 2: Traverse in both directions
        # Time: O(n), Space: O(1)

        n = len(nums) 

        left_to_right = 1
        right_to_left = 1

        maxProd = float("-inf")

        for i in range(n):

            # condition on seeing a zero
            if left_to_right == 0:
                left_to_right = 1
            if right_to_left == 0:
                right_to_left = 1


            j = n - i - 1
            left_to_right *= nums[i]
            right_to_left *= nums[j]

            maxProd = max(right_to_left, left_to_right, maxProd)

        return maxProd