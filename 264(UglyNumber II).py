class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]  # Initialize ugly numbers list with 1
        i2 = i3 = i5 = 0  # Pointers for multiples of 2, 3, and 5

        while len(ugly) < n:
            # Calculate the next multiples
            next2 = ugly[i2] * 2
            next3 = ugly[i3] * 3
            next5 = ugly[i5] * 5

            # Pick the smallest one to ensure sorted order
            next_ugly = min(next2, next3, next5)
            ugly.append(next_ugly)

            # Increment respective pointers
            if next_ugly == next2:
                i2 += 1
            if next_ugly == next3:
                i3 += 1
            if next_ugly == next5:
                i5 += 1

        return ugly[-1]


'''

Three Pointers Approach:
i2 tracks multiples of 2.
i3 tracks multiples of 3.
i5 tracks multiples of 5.
Next Ugly Calculation:
Pick the smallest value from 2 * ugly[i2], 3 * ugly[i3], and 5 * ugly[i5].
Increment the corresponding pointer(s) when the next ugly number matches a calculated multiple.
Repeat until you reach the Nth ugly number.


Time Complexity: O(n)
Space Complexity: O(n)
'''

