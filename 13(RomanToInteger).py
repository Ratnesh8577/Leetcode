class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary to map Roman numerals to integer values
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        summ = 0  # Variable to store the final integer value
        i = 0  # Pointer to traverse the string
        n = len(s)  # Length of the input string

        while i < n:
            # If current numeral is smaller than the next numeral, subtract its value
            if i < n - 1 and d[s[i]] < d[s[i + 1]]:
                summ += d[s[i + 1]] - d[s[i]]
                i += 2  # Move two steps ahead
            else:
                summ += d[s[i]]
                i += 1  # Move one step ahead
        
        return summ
# Time Complexity: O(n) (because we traverse the string once)
# Space Complexity: O(1) (since we use a fixed dictionary)