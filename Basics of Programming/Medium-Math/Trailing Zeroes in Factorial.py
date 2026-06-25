class Solution:
    def trailingZeroes(self, n):
        # code here
        count = 0
        i = 5

        while n // i > 0:
            count += n // i
            i *= 5

        return count