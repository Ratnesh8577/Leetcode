class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Handle cases where k > n
        
        # Rotate the array by shifting elements
        for _ in range(k):
            # Take the last element
            last = nums[-1]
            # Shift all elements to the right by one position
            for i in range(n - 1, 0, -1):
                nums[i] = nums[i - 1]
            # Place the last element at the first position
            nums[0] = last
        return nums
        