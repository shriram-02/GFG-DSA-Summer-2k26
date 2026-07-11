class Solution:
    def knightTour(self, n):
        board = [[-1] * n for _ in range(n)]

        moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]

        def valid(x, y):
            return 0 <= x < n and 0 <= y < n and board[x][y] == -1

        def degree(x, y):
            cnt = 0
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if valid(nx, ny):
                    cnt += 1
            return cnt

        def solve(x, y, step):
            board[x][y] = step
            if step == n * n - 1:
                return True

            nxt = []
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if valid(nx, ny):
                    nxt.append((degree(nx, ny), nx, ny))
            nxt.sort()

            for _, nx, ny in nxt:
                if solve(nx, ny, step + 1):
                    return True

            board[x][y] = -1
            return False

        solve(0, 0, 0)
        return board