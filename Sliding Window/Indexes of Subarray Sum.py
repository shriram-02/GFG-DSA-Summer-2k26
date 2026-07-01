class Solution:
    def subarraySum(self, arr, target):
        left = 0
        curr = 0

        for right in range(len(arr)):
            curr += arr[right]

            while curr > target and left <= right:
                curr -= arr[left]
                left += 1

            if curr == target:
                return [left + 1, right + 1]

        return [-1]