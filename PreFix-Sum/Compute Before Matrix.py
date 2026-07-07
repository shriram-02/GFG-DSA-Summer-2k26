class Solution:
    def computeBeforeMatrix(self, N, M, after):
        before = [[0] * M for _ in range(N)]

        for i in range(N):
            for j in range(M):
                before[i][j] = after[i][j]
                if i > 0:
                    before[i][j] -= after[i - 1][j]
                if j > 0:
                    before[i][j] -= after[i][j - 1]
                if i > 0 and j > 0:
                    before[i][j] += after[i - 1][j - 1]

        return before