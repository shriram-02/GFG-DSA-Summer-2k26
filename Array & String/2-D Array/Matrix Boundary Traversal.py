class Solution:
    def boundaryTraversal(self, mat):
        # code here
        n = len(mat)
        m = len(mat[0])

        res = []

        # Top row
        for j in range(m):
            res.append(mat[0][j])

        # Right column
        for i in range(1, n):
            res.append(mat[i][m - 1])

        # Bottom row
        if n > 1:
            for j in range(m - 2, -1, -1):
                res.append(mat[n - 1][j])

        # Left column
        if m > 1:
            for i in range(n - 2, 0, -1):
                res.append(mat[i][0])

        return res