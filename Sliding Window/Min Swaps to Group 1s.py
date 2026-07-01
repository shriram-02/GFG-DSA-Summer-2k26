class Solution:
    def minSwaps(self, arr):
        ones = sum(arr)
        if ones == 0:
            return -1

        bad = arr[:ones].count(0)
        ans = bad

        for i in range(ones, len(arr)):
            if arr[i - ones] == 0:
                bad -= 1
            if arr[i] == 0:
                bad += 1
            ans = min(ans, bad)

        return ans