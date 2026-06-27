class Solution:
    def sortBySetBitCount(self, arr):
        # code here
        arr.sort(key=lambda x: x.bit_count(), reverse=True)