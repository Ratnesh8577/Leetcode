"""class Solution:
    def countOdds(self, low: int, high: int) -> int:
        i=low
        count=0
        while i<=high:
            if i%2!=0:
                count+=1
            i+=1
        return count
        """
"""
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + (1 if low % 2 != 0 or high % 2 != 0 else 0)

"""

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Number of integers in the range
        length = high - low + 1
        
        # Half of the numbers are odd (integer division)
        half = length // 2
        
        # If either low or high is odd, add 1 more odd number
        if low % 2 == 1 or high % 2 == 1:
            return half + 1
        else:
            return half

# 4th method
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Find the first odd number >= low
        if low % 2 == 0:
            low += 1
        
        count = 0
        for num in range(low, high + 1, 2):
            count += 1
        return count

