class Solution:
    def reverseInGroups(self, arr, k):
        n = len(arr)

        for i in range(0, n, k):
            arr[i:min(i + k, n)] = arr[i:min(i + k, n)][::-1]

        return arr