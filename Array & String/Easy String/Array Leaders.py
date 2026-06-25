class Solution:
    def leaders(self, arr):
        res = []
        maxi = arr[-1]

        res.append(maxi)

        for i in range(len(arr) - 2, -1, -1):
            if arr[i] >= maxi:
                maxi = arr[i]
                res.append(arr[i])

        return res[::-1]