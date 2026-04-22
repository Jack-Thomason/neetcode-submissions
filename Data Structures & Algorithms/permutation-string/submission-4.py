class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        for i in range(m):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1_count[i] == window_count[i]:
                matches += 1

        if matches == 26:
            return True

        for i in range(m, n):
            add_idx = ord(s2[i]) - ord('a')
            remove_idx = ord(s2[i - m]) - ord('a')

            # add new char
            window_count[add_idx] += 1
            if window_count[add_idx] == s1_count[add_idx]:
                matches += 1
            elif window_count[add_idx] == s1_count[add_idx] + 1:
                matches -= 1

            # remove old char
            window_count[remove_idx] -= 1
            if window_count[remove_idx] == s1_count[remove_idx]:
                matches += 1
            elif window_count[remove_idx] == s1_count[remove_idx] - 1:
                matches -= 1

            if matches == 26:
                return True

        return False