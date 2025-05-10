class Solution:
    def largestNumber(self, nums):
        # Convert all numbers to strings
        nums = list(map(str, nums))
        
        # Sort using a key that simulates the comparison logic
        # Repeat each number's string to a fixed length to simulate comparison
        nums.sort(key=lambda x: x*10, reverse=True)
        
        # Edge case: all zeros
        if nums[0] == '0':
            return '0'
        
        return ''.join(nums)
