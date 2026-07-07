class Solution:
    def applyDiff2D(self, mat, opr):
        n = len(mat)
        m = len(mat[0])

        diff = [[0] * (m + 1) for _ in range(n + 1)]

        for r1, c1, r2, c2, val in opr:
            diff[r1][c1] += val
            if c2 + 1 < m:
                diff[r1][c2 + 1] -= val
            if r2 + 1 < n:
                diff[r2 + 1][c1] -= val
            if r2 + 1 < n and c2 + 1 < m:
                diff[r2 + 1][c2 + 1] += val

        for i in range(n):
            for j in range(1, m):
                diff[i][j] += diff[i][j - 1]

        for j in range(m):
            for i in range(1, n):
                diff[i][j] += diff[i - 1][j]

        for i in range(n):
            for j in range(m):
                mat[i][j] += diff[i][j]

        return mat