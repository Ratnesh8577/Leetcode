class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        missing_count = 0  # Count of missing numbers
        current = 1         # Current number to check
        
        # Iterate until we find k missing numbers
        for num in arr:
            # Count missing numbers between current and the next number in arr
            while current < num:
                missing_count += 1
                # If we've found k missing numbers, return the current number
                if missing_count == k:
                    return current
                current += 1
            # Move current to the next number after the current element in arr
            current += 1
        
        # If we reach here, the kth missing number is beyond the last element in arr
        return current + (k - missing_count - 1)
        