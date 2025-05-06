class Solution(object):
    def setZeroes(self, matrix):
        r = len(matrix)
        c = len(matrix[0])

        # First, mark the rows and columns that need to be zeroed
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    # Mark rows and columns with a placeholder (e.g., None)
                    for k in range(c):
                        if matrix[i][k] != 0:
                            matrix[i][k] = None
                    for k in range(r):
                        if matrix[k][j] != 0:
                            matrix[k][j] = None

        # Now set all placeholder values to 0
        for i in range(r):
            for j in range(c):
                if matrix[i][j] is None:
                    matrix[i][j] = 0


"""class Solution(object):
    def setZeroes(self, matrix):
        r = len(matrix)
        c = len(matrix[0])
        rows = set()
        cols = set()

        # First pass: find rows and columns that need to be zeroed
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Second pass: set rows to zero
        for i in rows:
            for j in range(c):
                matrix[i][j] = 0

        # Third pass: set columns to zero
        for j in cols:
            for i in range(r):
                matrix[i][j] = 0
"""