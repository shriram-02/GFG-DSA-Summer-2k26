class Solution:
    def countIncreasing(self, arr):
        ans = 0
        cnt = 0

        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                cnt += 1
            else:
                ans += cnt * (cnt + 1) // 2
                cnt = 0

        ans += cnt * (cnt + 1) // 2
        return ans