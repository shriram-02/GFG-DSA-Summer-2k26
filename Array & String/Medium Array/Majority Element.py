class Solution:
    def majorityElement(self, arr):
        # code here
        candidate = None
        count = 0

        for num in arr:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        if arr.count(candidate) > len(arr) // 2:
            return candidate

        return -1