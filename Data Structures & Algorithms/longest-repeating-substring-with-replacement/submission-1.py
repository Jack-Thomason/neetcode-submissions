class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        maxF = 0
        l = 0
        ans = 0

        for r, char in enumerate(s):
            freq[char] += 1
            maxF = max(maxF, freq[char])

            while (r - l + 1) - maxF > k:
                freq[s[l]] -= 1
                l += 1 
            
            ans = max(ans, (r - l + 1))
        
        return ans
        