class Solution:
    def isThree(self, n: int) -> bool:
         #  perfect square
        root = int(n**0.5)
        if root * root != n:
            return False
        
        #  square root is prime
        if root < 2:
            return False
        
        for i in range(2, int(root**0.5) + 1):
            if root % i == 0:
                return False
        
        return True
        