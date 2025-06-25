class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 1
        while x < n:
            x = (x << 1) | 1  # Builds numbers like 1 (1), 3 (11), 7 (111), 15 (1111), etc.
        return x
