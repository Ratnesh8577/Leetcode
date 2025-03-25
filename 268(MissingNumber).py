class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        # Calculate the expected sum of numbers from 0 to n
        total_sum = n * (n + 1) // 2
        # Calculate the actual sum of numbers in the array
        actual_sum = sum(nums)
        # The difference is the missing number
        return total_sum - actual_sum



'''
Time Complexity: O(n)
Space Complexity: O(1)
'''