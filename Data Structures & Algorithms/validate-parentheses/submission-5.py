class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"}":"{", ")":"(", "]":"["}
        

        for char in s:
            if char in d.values():
                stack.append(char)
            elif char in d:
                if not stack or stack.pop() != d[char]:
                    return False
        return not stack