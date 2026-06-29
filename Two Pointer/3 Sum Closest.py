class Solution:
    def closest3Sum(self, arr, target):
        arr.sort()
        n = len(arr)
        best = arr[0] + arr[1] + arr[2]

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                s = arr[i] + arr[left] + arr[right]

                if abs(s - target) < abs(best - target) or (
                    abs(s - target) == abs(best - target) and s > best
                ):
                    best = s

                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    return s

        return best