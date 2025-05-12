"""class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
       
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
        """
class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  # Handle cases where k > n
        
        # Reverse the entire array
        nums.reverse()
        
        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])
        
        # Reverse the remaining n - k elements
        nums[k:] = reversed(nums[k:])
        
        return nums
