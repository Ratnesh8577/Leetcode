class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Special case: if only one row, return the original string
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list of empty strings for each row
        rows = [''] * numRows
        curr_row = 0
        going_down = False

        # Traverse the input string and place characters in the appropriate row
        for char in s:
            rows[curr_row] += char
            # Change direction if we are at the first or last row
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down
            # Move up or down depending on direction
            curr_row += 1 if going_down else -1

        # Concatenate all rows to get the final result
        return ''.join(rows)
