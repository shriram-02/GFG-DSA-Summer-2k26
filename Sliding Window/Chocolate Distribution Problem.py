class Solution:
    def findMinDiff(self, arr, m):
        n = len(arr)
        if m == 0 or n == 0:
            return 0

        arr.sort()
        ans = float('inf')

        for i in range(n - m + 1):
            ans = min(ans, arr[i + m - 1] - arr[i])

        return ans