	class Solution:
    def countSubarray(self, arr, k):
        if k <= 1:
            return 0

        left = 0
        prod = 1
        ans = 0

        for right in range(len(arr)):
            prod *= arr[right]

            while prod >= k:
                prod //= arr[left]
                left += 1

            ans += right - left + 1

        return ans