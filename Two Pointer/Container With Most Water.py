class Solution:
    def maxWater(self, arr):
        left, right = 0, len(arr) - 1
        ans = 0

        while left < right:
            ans = max(ans, min(arr[left], arr[right]) * (right - left))

            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1

        return ans