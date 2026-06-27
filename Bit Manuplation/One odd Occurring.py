class Solution:
    def getOddOccurrence(self, arr):
        # code here
        ans = 0
        for x in arr:
            ans ^= x
        return ans