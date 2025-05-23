from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if n == k:
            return sum(cardPoints)

        left_sum = 0
        right_sum = 0

        # Initial left sum from first k cards
        for i in range(0, k):
            left_sum += cardPoints[i]

        maxi = left_sum
        right_index = n - 1

        # Now slide the window: take i from right, (k - i) from left
        for i in range(1, k + 1):
            left_sum -= cardPoints[k - i]
            right_sum += cardPoints[right_index]
            current = left_sum + right_sum
            maxi = max(maxi, current)
            right_index -= 1

        return maxi
