"""class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        result = 0
        current_sum = 1
        i = 0
        n = len(coins)

        while current_sum <= target:
            if i < n and coins[i] <= current_sum:
                current_sum += coins[i]
                i += 1
            else:
                result += 1
                current_sum *= 2
        return result
"""
class Solution:
    def minimumAddedCoins(self, coins: list[int], target: int) -> int:
        coins.sort()
        added_coins = 0
        max_reachable = 1
        i = 0
        n = len(coins)
        
        while max_reachable <= target:
            if i < n and coins[i] <= max_reachable:
                max_reachable += coins[i]
                i += 1
            else:
                # Add a coin of value max_reachable
                added_coins += 1
                max_reachable *= 2
        return added_coins
