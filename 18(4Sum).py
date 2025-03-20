class Solution:
    def fourSum(self, nums, target):  # Function to find all unique quadruplets that sum to target
        n = len(nums)  # Get the length of the array
        answer = []  # Initialize a list to store valid quadruplets
        nums.sort()  # Sort the array to make it easier to use two-pointer approach

        for i in range(n):  # First loop: Fix the first number
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate values to avoid repeated quadruplets
                continue

            for j in range(i + 1, n):  # Second loop: Fix the second number
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicate values for the second number
                    continue

                lo, hi = j + 1, n - 1  # Two-pointer approach: lo starts after j, hi starts at end

                while lo < hi:  # While two pointers don't cross
                    summ = nums[i] + nums[j] + nums[lo] + nums[hi]  # Calculate the sum of four numbers

                    if summ == target:  # If sum matches target, store the quadruplet
                        answer.append([nums[i], nums[j], nums[lo], nums[hi]])

                        lo += 1  # Move lo pointer forward
                        hi -= 1  # Move hi pointer backward

                        while lo < hi and nums[lo] == nums[lo - 1]:  # Skip duplicate values for lo
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi + 1]:  # Skip duplicate values for hi
                            hi -= 1

                    elif summ < target:  # If sum is smaller than target, increase lo to get a larger sum
                        lo += 1
                    else:  # If sum is greater than target, decrease hi to get a smaller sum
                        hi -= 1

        return answer  # Return the list of unique quadruplets

        # Time Complexity: O(n^3) -> Three loops and a two-pointer approach inside
        # Space Complexity: O(1) -> No extra space used apart from the output list


# Sample Test Case to Run in VS Code
if __name__ == "__main__":
    solution = Solution()
    
    # Example Input
    nums = [1, 0, -1, 0, -2, 2]
    target = 0

    # Run the function and print the result
    print(solution.fourSum(nums, target))
