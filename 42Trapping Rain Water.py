class Solution:
    def trap(self, height):  # Function to calculate trapped rainwater
        l_wall = r_wall = 0  # Initialize left and right max heights to 0
        n = len(height)  # Get the length of the height array
        max_left = [0] * n  # Create an array to store max height from the left
        max_right = [0] * n  # Create an array to store max height from the right

        # First pass: Compute max_left and max_right
        for i in range(n):  
            j = -i - 1  # Index from the end (same as n-1-i)
            max_left[i] = l_wall  # Store the max height seen so far from the left
            max_right[j] = r_wall  # Store the max height seen so far from the right
            l_wall = max(l_wall, height[i])  # Update left max height
            r_wall = max(r_wall, height[j])  # Update right max height

        summ = 0  # Initialize total trapped water to 0
        for i in range(n):  # Second pass: Calculate trapped water
            pot = min(max_left[i], max_right[i])  # Find the min height of walls on both sides
            summ += max(0, pot - height[i])  # Add trapped water if pot is greater than height[i]

        return summ  # Return the total trapped water

        # Time Complexity: O(n) -> We traverse the array twice (once for max_left/max_right, once for water calculation)
        # Space Complexity: O(n) -> We use extra space for max_left and max_right arrays
