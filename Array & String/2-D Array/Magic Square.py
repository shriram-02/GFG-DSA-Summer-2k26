class Solution:
    def magicSquare(self, mat):
        # code here
        n = len(mat)

        target = sum(mat[0])

        for i in range(n):
            if sum(mat[i]) != target:
                return False

        for j in range(n):
            if sum(mat[i][j] for i in range(n)) != target:
                return False

        if sum(mat[i][i] for i in range(n)) != target:
            return False

        if sum(mat[i][n - 1 - i] for i in range(n)) != target:
            return False

        return True