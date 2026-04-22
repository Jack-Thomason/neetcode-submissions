class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)

        if m > n:
            return False
        
        window_count = [0] * 26
        s1_count = [0] * 26

        for i in range(m):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1
        
        if s1_count == window_count:
            return True
        
        for i in range(m, n):
            window_count[ord(s2[i]) - ord('a')] += 1
            window_count[ord(s2[i - m]) - ord('a')] -= 1
        
            if window_count == s1_count:
                return True
        
        return False