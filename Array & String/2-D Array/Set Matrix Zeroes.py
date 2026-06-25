class Solution:
    def setMatrixZeroes(self, mat):
        # code here
        rows = len(mat)
        cols = len(mat[0])

        zero_rows = set()
        zero_cols = set()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for i in range(rows):
            for j in range(cols):
                if i in zero_rows or j in zero_cols:
                    mat[i][j] = 0

        return mat