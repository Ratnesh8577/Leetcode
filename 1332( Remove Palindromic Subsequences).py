"""class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # Check if s is a palindrome
        if s == s[::-1]:
            return 1
        else:
            return 2

"""
"""class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # If s is empty, no steps needed
        if not s:
            return 0
        
        # If s is already a palindrome
        if s == s[::-1]:
            return 1
        
        # If s contains both 'a' and 'b', minimum steps is 2
        # Because you remove all 'a's in one step, and all 'b's in another
        return 2
"""

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        # Base case: single characters are palindromes themselves, 1 step to remove
        for i in range(n):
            dp[i][i] = 1
        
        for length in range(2, n + 1):  # substring lengths
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] if length > 2 else 1
                else:
                    dp[i][j] = min(dp[i][k] + dp[k + 1][j] for k in range(i, j))
        
        return dp[0][n - 1]

