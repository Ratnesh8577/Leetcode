class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle edge case where result exceeds bounds
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine the sign of the quotient
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        
        # Bitwise subtraction method (exponential search)
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            dividend -= temp
            quotient += multiple
        
        # Apply sign
        if negative:
            quotient = -quotient
        
        return max(INT_MIN, min(INT_MAX, quotient))

        
        