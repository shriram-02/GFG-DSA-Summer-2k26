class Solution:
    def fourSum(self, arr, target):
        arr.sort()
        n = len(arr)
        res = []

        for i in range(n - 3):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue

                left, right = j + 1, n - 1

                while left < right:
                    s = arr[i] + arr[j] + arr[left] + arr[right]

                    if s == target:
                        res.append([arr[i], arr[j], arr[left], arr[right]])
                        left += 1
                        right -= 1

                        while left < right and arr[left] == arr[left - 1]:
                            left += 1
                        while left < right and arr[right] == arr[right + 1]:
                            right -= 1

                    elif s < target:
                        left += 1
                    else:
                        right -= 1

        return res