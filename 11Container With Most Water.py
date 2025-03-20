from typing import List  # Import List for type hinting

class Solution:
    def maxArea(self, height: List[int]) -> int:  # Define the function to find max water area
        n = len(height)  # Get the length of the height array
        l = 0  # Initialize the left pointer at the beginning
        r = n - 1  # Initialize the right pointer at the end
        max_area = 0  # Variable to store the maximum area found

        while l < r:  # Continue while left pointer is less than right pointer
            w = r - l  # Calculate the width of the container
            h = min(height[l], height[r])  # Find the minimum height between left and right
            a = w * h  # Compute the area
            max_area = max(max_area, a)  # Update max_area if the current area is larger

            if height[l] < height[r]:  # Move the pointer with the smaller height
                l += 1  # Move the left pointer right
            else:
                r -= 1  # Move the right pointer left
                
        return max_area  # Return the maximum area found

        # Time Complexity: O(n) -> We traverse the array once with two pointers
        # Space Complexity: O(1) -> Only a few variables are used, no extra space required
