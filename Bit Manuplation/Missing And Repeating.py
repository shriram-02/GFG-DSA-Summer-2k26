class Solution:
    def findTwoElement(self, arr):
        # code here
        n = len(arr)
        s = n * (n + 1) // 2
        ss = n * (n + 1) * (2 * n + 1) // 6

        arr_sum = sum(arr)
        arr_sq_sum = sum(x * x for x in arr)

        diff = arr_sum - s          # repeating - missing
        sq_diff = arr_sq_sum - ss   # repeating² - missing²

        sum_rm = sq_diff // diff

        repeating = (diff + sum_rm) // 2
        missing = repeating - diff

        return [repeating, missing]