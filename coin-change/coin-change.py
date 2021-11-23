class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        check = {}
        if amount < 0:
            return 0
    
    
        def yo(coins, amount):
            if amount in check:
                return check[amount]
            if amount == 0:
                return 0
            if amount < 0:
                return -1

            shortest = -1

            for i in coins:
                remainder = amount - i
                remainderCombo = yo(coins, remainder)
                if remainderCombo != -1:
                    combo = remainderCombo + 1
                    if shortest == -1 or combo < shortest:
                        shortest = combo

            check[amount] = shortest
            return shortest
        
        return yo(coins,amount)