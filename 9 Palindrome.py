class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False  
        
        summ = 0  # Variable to store the reversed number
        original = x  # Store the original value of x
        
        while x > 0:  # Loop until x becomes 0
            digit = x % 10  # Extract the last digit
            summ = (summ * 10) + digit  # Append the digit to the reversed number
            x = x // 10  # Remove the last digit from x
        
        # If the reversed number is the same as the original, it's a palindrome
        return summ == original

# Testing the function
sol = Solution()
test_cases = [121, -121, 10, 0, 1221, 12321, 123]
for num in test_cases:
    print(f"{num} is a palindrome? {sol.isPalindrome(num)}")
