class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_map = "0123456789abcdef"

        # Convert negative number using two's complement
        if num < 0:
            num += 2**32

        result = ""
        while num > 0:
            digit = num % 16
            result = hex_map[digit] + result
            num //= 16

        return result
