class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)  # Length of the list
        i = 0  # Left pointer
        j = n - 1  # Right pointer
        
        while i <= j:
            m = (i + j) // 2  # Calculate the middle index
            
            if nums[m] < target:
                i = m + 1  # Move the left pointer to the right of mid
            elif nums[m] > target:
                j = m - 1  # Move the right pointer to the left of mid
            else:
                return m  # Target found, return the index
        
        # If target is not found, return the appropriate insert position
        return i

# Time Complexity: O(log N) due to binary search
# Space Complexity: O(1) as no extra space is used