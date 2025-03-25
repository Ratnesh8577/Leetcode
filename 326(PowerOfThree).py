class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Base case: n must be greater than 0
        if n <= 0:
            return False
        
        # Check if 3^x = n by continuously dividing n by 3
        while n % 3 == 0:
            n //= 3
        
        # If n becomes 1, it's a power of 3
        return n == 1

'''
Time Complexity: O(log₃(n)) 
Space Complexity: O(1).''
'''