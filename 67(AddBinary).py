class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        
        result = []
        carry = 0
        
        # Traverse both strings from right to left
        for i in range(max_len - 1, -1, -1):
            total = carry + int(a[i]) + int(b[i])
            result.append(str(total % 2))  # Append the remainder (0 or 1)
            carry = total // 2  # Update carry (0 or 1)

        # If there's still a carry left, add it to the result
        if carry:
            result.append('1')

        # Reverse the result to get the final binary string
        return ''.join(result[::-1])
        