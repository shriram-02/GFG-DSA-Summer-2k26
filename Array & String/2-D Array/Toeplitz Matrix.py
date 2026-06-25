class Solution:
    def isToeplitz(self, mat):
        # code here
        n = len(mat)
        m = len(mat[0])

        for i in range(1, n):
            for j in range(1, m):
                if mat[i][j] != mat[i - 1][j - 1]:
                    return False

        return True