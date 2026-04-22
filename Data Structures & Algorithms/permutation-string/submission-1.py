class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = [0] * 26

        for ch in s1:
            s1_count[ord(ch) - ord('a')] += 1

        for i in range(len(s2) - len(s1) + 1):
            freq_count = [0] * 26
            j = i + len(s1) 
            for ch in s2[i:j]:
                freq_count[ord(ch) - ord('a')] += 1
            if freq_count == s1_count:
                return True
        
        return False



        
        


        