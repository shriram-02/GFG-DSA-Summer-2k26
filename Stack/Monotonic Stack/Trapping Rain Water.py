class Solution:
    def maxWater(self, arr):
        l, r = 0, len(arr) - 1
        lm = rm = 0
        ans = 0

        while l <= r:
            if arr[l] <= arr[r]:
                if arr[l] >= lm:
                    lm = arr[l]
                else:
                    ans += lm - arr[l]
                l += 1
            else:
                if arr[r] >= rm:
                    rm = arr[r]
                else:
                    ans += rm - arr[r]
                r -= 1
        return ans