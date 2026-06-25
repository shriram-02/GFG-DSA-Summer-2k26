class Solution:
    def printPat(self, n):
        # Upper half (including middle)
        for i in range(n):
            print(" " * (n - i - 1), end="")
            if i == 0:
                print("*")
            else:
                print("*" + " " * (2 * i - 1) + "*")

        # Lower half (mirror, excluding middle row)
        for i in range(n - 2, -1, -1):
            print(" " * (n - i - 1), end="")
            if i == 0:
                print("*")
            else:
                print("*" + " " * (2 * i - 1) + "*")