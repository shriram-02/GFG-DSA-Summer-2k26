class Solution:
    def find3Numbers(self, arr):
        # code here
        n = len(arr)

        smaller = [-1] * n
        greater = [-1] * n

        min_idx = 0
        for i in range(1, n):
            if arr[i] <= arr[min_idx]:
                min_idx = i
            else:
                smaller[i] = min_idx

        max_idx = n - 1
        for i in range(n - 2, -1, -1):
            if arr[i] >= arr[max_idx]:
                max_idx = i
            else:
                greater[i] = max_idx

        for i in range(n):
            if smaller[i] != -1 and greater[i] != -1:
                return [arr[smaller[i]], arr[i], arr[greater[i]]]

        return []