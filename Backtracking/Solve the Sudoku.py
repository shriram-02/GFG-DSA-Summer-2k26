class Solution:
    def solveSudoku(self, mat):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if mat[i][j] != 0:
                    rows[i].add(mat[i][j])
                    cols[j].add(mat[i][j])
                    boxes[(i // 3) * 3 + j // 3].add(mat[i][j])

        def solve():
            for i in range(9):
                for j in range(9):
                    if mat[i][j] == 0:
                        b = (i // 3) * 3 + j // 3
                        for num in range(1, 10):
                            if num not in rows[i] and num not in cols[j] and num not in boxes[b]:
                                mat[i][j] = num
                                rows[i].add(num)
                                cols[j].add(num)
                                boxes[b].add(num)

                                if solve():
                                    return True

                                mat[i][j] = 0
                                rows[i].remove(num)
                                cols[j].remove(num)
                                boxes[b].remove(num)
                        return False
            return True

        solve()