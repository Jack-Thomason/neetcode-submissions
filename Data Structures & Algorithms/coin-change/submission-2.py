class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        

        def minCoinRec(i, amount, coins, memo):
            if amount == 0:
                return 0
            if amount < 0 or i == len(coins):
                return float("inf")

            if memo[i][amount] != -1:
                return memo[i][amount]

            if coins[i] > 0:
                take = minCoinRec(i, amount - coins[i], coins, memo)
                if take != float("inf"):
                    take += 1
                noTake = minCoinRec(i + 1, amount, coins, memo)
            
            memo[i][amount] = min(take, noTake)

            return memo[i][amount]
        
        memo = [[-1] * (amount + 1) for _ in range(len(coins))]
        ans = minCoinRec(0, amount, coins, memo)
        return ans if ans != float("inf") else -1

    

    

    
        