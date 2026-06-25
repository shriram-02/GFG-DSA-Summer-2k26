class Solution:
    def subarraySum(self, arr):
        n = len(arr)
        ans = 0

        for i in range(n):
            ans += arr[i] * (i + 1) * (n - i)

        return ans