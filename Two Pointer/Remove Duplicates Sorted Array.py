class Solution:
    def removeDuplicates(self, arr):
        if not arr:
            return []

        res = [arr[0]]
        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1]:
                res.append(arr[i])

        return res