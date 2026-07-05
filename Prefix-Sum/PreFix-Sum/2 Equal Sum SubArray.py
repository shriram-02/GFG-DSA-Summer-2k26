class Solution:
    def canSplit(self, arr):
        # code here
        total = sum(arr)
        
        if total % 2:
            return False
        
        curr = 0
        
        for num in arr[:-1]:
            curr += num
            if curr == total // 2:
                return True
        
        return False