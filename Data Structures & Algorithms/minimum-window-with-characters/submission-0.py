class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)
        missing = len(t)

        l = 0
        best_len = float("inf")
        best_l = 0

        for r, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            while missing == 0:
                window_len = r - l + 1
                if window_len < best_len:
                    best_len = window_len
                    best_l = l
                left_char = s[l]
                need[left_char] += 1
                if need[left_char] > 0:
                    missing += 1
                l += 1

        return "" if best_len == float("inf") else s[best_l:best_l + best_len]