class Solution:
    def maxConsecutiveBits(self, arr):
        # code here
        ans = cnt = 1

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)

        return ans