class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0

        seen = {}

        for r, char in enumerate(s):

            if char in seen:
                l = max(l, seen[char] + 1)
            
            seen[char] = r
            longest = max(longest, r - l + 1)

        return longest  

