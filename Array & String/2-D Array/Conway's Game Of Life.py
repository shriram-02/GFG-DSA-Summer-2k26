class Solution:
    def findNextGen(self, mat):
        # code here
        m = len(mat)
        n = len(mat[0])

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]

        temp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                live = 0

                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n:
                        live += mat[ni][nj]

                if mat[i][j] == 1:
                    if live == 2 or live == 3:
                        temp[i][j] = 1
                else:
                    if live == 3:
                        temp[i][j] = 1

        for i in range(m):
            for j in range(n):
                mat[i][j] = temp[i][j]