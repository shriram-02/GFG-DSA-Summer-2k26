class Solution:
    def maxSubarraySum(self, arr):
        curr = maxi = arr[0]

        for i in range(1, len(arr)):
            curr = max(arr[i], curr + arr[i])
            maxi = max(maxi, curr)

        return maxi