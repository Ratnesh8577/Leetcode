class Solution:
    def isUgly(self, n: int) -> bool:
        # An ugly number must be positive
        if n <= 0:
            return False
        # Divide n by 2, 3, and 5 as much as possible
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
        
        # If after removing all 2, 3, and 5 factors n becomes 1, it's an ugly number
        return n == 1
        
        