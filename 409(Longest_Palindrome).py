class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter

        freq = Counter(s)
        length = 0
        odd_found = False

        for count in freq.values():
            # Add the largest even part of the count
            length += (count // 2) * 2
            # If there's an odd count, we can use one character in the center
            if count % 2 == 1:
                odd_found = True

        # Add one character in the center if any odd character exists
        if odd_found:
            length += 1

        return length
