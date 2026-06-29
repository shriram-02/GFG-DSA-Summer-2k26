class Solution:
    def celebrity(self, mat):
        n = len(mat)
        cand = 0

        for i in range(1, n):
            if mat[cand][i] == 1:
                cand = i

        for i in range(n):
            if i != cand:
                if mat[cand][i] == 1 or mat[i][cand] == 0:
                    return -1

        return cand