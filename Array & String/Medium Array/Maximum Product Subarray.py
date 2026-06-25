class Solution:
    def maxProduct(self, arr):
        max_prod = min_prod = ans = arr[0]

        for i in range(1, len(arr)):
            if arr[i] < 0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(arr[i], max_prod * arr[i])
            min_prod = min(arr[i], min_prod * arr[i])

            ans = max(ans, max_prod)

        return ans