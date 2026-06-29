class Solution:
    def hasTripletSum(self, arr, target):
        arr.sort()
        n = len(arr)

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                s = arr[i] + arr[left] + arr[right]

                if s == target:
                    return True
                elif s < target:
                    left += 1
                else:
                    right -= 1

        return False