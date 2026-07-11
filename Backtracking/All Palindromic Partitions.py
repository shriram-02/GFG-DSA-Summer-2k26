class Solution:
    def palinParts(self, s):
        ans = []
        path = []

        def isPal(x):
            return x == x[::-1]

        def dfs(idx):
            if idx == len(s):
                ans.append(path[:])
                return

            for j in range(idx + 1, len(s) + 1):
                part = s[idx:j]
                if isPal(part):
                    path.append(part)
                    dfs(j)
                    path.pop()

        dfs(0)
        return ans