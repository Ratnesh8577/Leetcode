"""class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove any trailing spaces, then split by spaces
        words = s.strip().split()
        # Return the length of the last word
        return len(words[-1])
"""

"""class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1

        # Step 1: Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Step 2: Count characters in the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        in_word = False

        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                length += 1
                in_word = True
            elif in_word:
                break

        return length
