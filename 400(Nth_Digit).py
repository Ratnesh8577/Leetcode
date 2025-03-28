class Solution:
    def findNthDigit(self, n: int) -> int:
        length = 1  # Length of numbers in the current range
        count = 9  # Count of numbers in the current range
        start = 1  # Starting number of the current range
        
        # Find the range where the nth digit lies
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10
        
        # Identify the exact number that contains the nth digit
        num = start + (n - 1) // length
        
        # Extract the nth digit from that number
        return int(str(num)[(n - 1) % length])

        