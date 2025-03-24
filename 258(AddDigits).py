class Solution:
    def addDigits(self, num: int) -> int:
        
        # Digital root formula
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
        

