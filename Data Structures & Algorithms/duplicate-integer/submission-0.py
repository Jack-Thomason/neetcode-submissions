class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = {}
        for i in nums:
            if s.get(i):
                return True
            else:
                s[i] = 1
                print(s)
        return False