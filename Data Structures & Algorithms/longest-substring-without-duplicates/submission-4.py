class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 1
        current = 0
        l = 0 
        if len(s) == 0:
            return 0

        seen = {s[l]: 0}

        for r in range(1, len(s)):
            if s[r] in seen:
                l = max(l, seen[s[r]] + 1)

            seen[s[r]] = r
            longest = max(longest, r - l + 1)


            

        
            

        return longest
        