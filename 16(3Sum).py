class Solution:
    def threeSumClosest(self, nums, target):
        # Sort the array to apply the two-pointer approach
        nums.sort()
        n = len(nums)
        # Initialize the closest sum to a very large value
        closest_sum = float("inf")

        # Iterate through each number in the array
        for i in range(n):
            # Skip duplicate elements to avoid redundant calculations
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize two pointers: lo and hi
            lo, hi = i + 1, n - 1

            # Use two pointers to find the closest sum for the current element
            while lo < hi:
                # Calculate the current sum of three numbers
                cur_sum = nums[i] + nums[lo] + nums[hi]

                # Update closest_sum if the current sum is closer to the target
                if abs(cur_sum - target) < abs(closest_sum - target):
                    closest_sum = cur_sum

                # If the exact target is found, return immediately
                if cur_sum == target:
                    return cur_sum
                # If the current sum is less than the target, move the lo pointer to increase the sum
                elif cur_sum < target:
                    lo += 1
                # If the current sum is greater than the target, move the hi pointer to decrease the sum
                else:
                    hi -= 1

        # Return the closest sum found
        return closest_sum
