class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_do(k) -> bool:
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k
                
            return hours <= h

        l, r = 1, max(piles)
        res = r

        while l < r:
            k = (l + r) // 2

            if can_do(k):
                r = k
            else: 
                l = k + 1

        return l


        
        

        




