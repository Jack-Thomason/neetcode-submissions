class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = (s[0], 0)

        def helper(l, r):
            temp = s[l:r+1]
            while l < r:
                if s[l] != s[r]:
                    return""
                l += 1
                r -= 1
            return temp

        for i in range(len(s)):
            l, r = i, len(s) - 1

            if r - l + 1 < palindrome[1]:
                continue
            while l < r:
                if s[l] == s[r]:
                    res = helper(l, r)
                    if len(res) > palindrome[1]:
                        palindrome = (res, len(res))
                        break
                r -= 1
        return palindrome[0]


        