class Solution:
    def printHollowRect(self, n, m):
        # code here
        for i in range(n):
            if m == 1:
                print("*")
            elif i == 0 or i == n - 1:
                print("*" * m)
            else:
                print("*" + " " * (m - 2) + "*")