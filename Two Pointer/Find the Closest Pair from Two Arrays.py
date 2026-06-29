class Solution:
    def findClosestPair(self, arr1, arr2, x):
        i, j = 0, len(arr2) - 1
        best = float('inf')
        ans = []

        while i < len(arr1) and j >= 0:
            s = arr1[i] + arr2[j]

            if abs(s - x) < best:
                best = abs(s - x)
                ans = [arr1[i], arr2[j]]

            if s > x:
                j -= 1
            else:
                i += 1

        return ans