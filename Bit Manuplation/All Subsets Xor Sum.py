class Solution:
    def subsetXORSum(self, arr):
        # code here
        OR = 0
        for x in arr:
            OR |= x
        return OR * (1 << (len(arr) - 1))