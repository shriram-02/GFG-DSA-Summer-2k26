class Solution:
    def getSubArrays(self, arr):
        res = []
        n = len(arr)

        for i in range(n):
            for j in range(i, n):
                res.append(arr[i:j + 1])

        return res