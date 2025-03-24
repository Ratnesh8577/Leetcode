class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        # Sort the input to handle duplicates
        nums.sort()
        result = []
        
        def backtrack(start, path):
            # Add the current path to the result
            result.append(path[:])
            
            # Explore further elements
            for i in range(start, len(nums)):
                # Skip duplicates at the same level
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # Include nums[i] and move forward
                path.append(nums[i])
                backtrack(i + 1, path)
                # Backtrack: remove the last element added
                path.pop()
        
        backtrack(0, [])
        return result
        