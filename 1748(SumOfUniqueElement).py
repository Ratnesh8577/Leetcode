class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
         # Use a dictionary 
        freq = {}
        
        #  each number in nums
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # Sum up numbers that appear only once
        unique_sum = sum(num for num, count in freq.items() if count == 1)
        
        return unique_sum
        