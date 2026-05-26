class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = Counter(s1)
        window = Counter()

        l = 0

        for r, char in enumerate(s2):
            window[char] += 1

            if r - l + 1 > len(s1):
                left_char = s2[l]
                window[left_char] -= 1

                if window[left_char] == 0:
                    del window[left_char]

                l += 1
            if need == window:
                return True
                
        return False

