class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        # Check if 3^x = n by continuously dividing n by 4
        while n % 4 == 0:
            n //= 4
        
        # If n becomes 1, it's a power of 4
        return n == 1
        