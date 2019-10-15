"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount<=0:
            return 0
        
        set_coins = set(coins)
        min_coin = min(coins)
        infeasible_num = 10000000
        split = {}
        
        def splitChangeHelper(amount):
            if amount in set_coins:
                return 1
            if amount < min_coin:
                return infeasible_num
            
            current_minimum = []
            
            for coin in coins:
                if amount-coin not in split:
                    split[amount-coin] = splitChangeHelper(amount-coin)
                current_minimum.append(split[amount-coin])
            
            return min(current_minimum) + 1
        count = splitChangeHelper(amount)
        
        if count >= infeasible_num:
            return -1
        return count
            