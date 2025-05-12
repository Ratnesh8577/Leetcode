class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)  # Convert string to list for in-place editing
        
        def reverse_substring(start: int, end: int):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        for i in range(0, len(s), 2 * k):
            # Reverse from index i to i + k - 1 (or end of string)
            reverse_substring(i, min(i + k - 1, len(s) - 1))
        
        return ''.join(s)

# 2nd Method
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ''
        
        for i in range(0, len(s), 2 * k):
            first_k = s[i:i + k][::-1]     # Reverse first k characters
            rest = s[i + k:i + 2 * k]      # Keep next k characters unchanged
            result += first_k + rest       # Append both to result
        
        return result

# 3rd Method
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        return ''.join(
            s[i:i + k][::-1] + s[i + k:i + 2 * k]
            for i in range(0, len(s), 2 * k)
        )
