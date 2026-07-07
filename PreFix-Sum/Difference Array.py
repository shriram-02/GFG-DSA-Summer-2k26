class Solution:
    def diffArray(self, arr, opr):
        n = len(arr)
        diff = [0] * (n + 1)

        for l, r, v in opr:
            diff[l] += v
            if r + 1 < n:
                diff[r + 1] -= v

        cur = 0
        for i in range(n):
            cur += diff[i]
            arr[i] += cur

        return arr