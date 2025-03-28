class Solution:
    def largestOddNumber(self, num: str) -> str:
         # Iterate from the end of the string to find the first odd digit
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]  # Return the largest odd substring
        return ""  # Return empty string if no odd number is found

        