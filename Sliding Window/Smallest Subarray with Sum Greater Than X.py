class Solution:
    def smallestSubWithSum(self, x, arr):
        left = 0
        curr = 0
        ans = float('inf')

        for right in range(len(arr)):
            curr += arr[right]

            while curr > x:
                ans = min(ans, right - left + 1)
                curr -= arr[left]
                left += 1

        return 0 if ans == float('inf') else ans