class Solution:
    def missingNum(self, arr):
        # code here
        n = len(arr) + 1
        return n * (n + 1) // 2 - sum(arr)