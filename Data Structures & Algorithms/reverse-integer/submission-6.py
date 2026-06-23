class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = (-2**31)
        INT_MAX = (2**31) - 1

        res = 0

        while x:
            
            # Pop last digit.
            if x > 0:
                digit = x % 10
            else:
                digit = x % -10
            x = int(x / 10)

            # Check positive overflow before multiplying by 10.
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0

            # Check negative overflow before multiplying by 10.
            if res < INT_MIN // 10 or (res == INT_MIN // 10 and digit < INT_MIN % 10):
                return 0

            

            

            # Push digit onto result.
            res = res * 10 + digit

        return res