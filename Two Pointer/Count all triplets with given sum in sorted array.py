class Solution:
    def countTriplets(self, arr, target):
        n = len(arr)
        ans = 0

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                s = arr[i] + arr[left] + arr[right]

                if s == target:
                    if arr[left] == arr[right]:
                        cnt = right - left + 1
                        ans += cnt * (cnt - 1) // 2
                        break

                    lcnt = 1
                    rcnt = 1

                    while left + 1 < right and arr[left] == arr[left + 1]:
                        lcnt += 1
                        left += 1

                    while right - 1 > left and arr[right] == arr[right - 1]:
                        rcnt += 1
                        right -= 1

                    ans += lcnt * rcnt
                    left += 1
                    right -= 1

                elif s < target:
                    left += 1
                else:
                    right -= 1

        return ans