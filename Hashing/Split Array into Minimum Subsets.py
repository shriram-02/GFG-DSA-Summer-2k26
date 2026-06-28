class Solution:
    def minSubsets(self, arr):
        arr.sort()
        cnt = 0

        for i in range(len(arr)):
            if i == 0 or arr[i] != arr[i - 1] + 1:
                cnt += 1

        return cnt