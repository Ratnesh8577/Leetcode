class Solution:
    def search(self, nums, target):
        n = len(nums)
        l, r = 0, n - 1  # Initialize left and right pointers
        
        # Step 1: Find the pivot (index of the smallest element)
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        min_i = l  # Pivot found

        # Step 2: Decide which part to search — left of pivot or right of pivot
        if target >= nums[min_i] and target <= nums[n - 1]:
            l, r = min_i, n - 1  # Search in the right sorted part
        else:
            l, r = 0, min_i - 1  # Search in the left sorted part

        # Step 3: Regular binary search in the chosen part
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m  # Target found, return index
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        # If target is not found, return -1
        return -1

# Time Complexity: O(log N) due to binary search
# Space Complexity: O(1) as no extra space is used
