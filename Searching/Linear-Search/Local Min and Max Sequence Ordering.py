class Solution:
    def extractPoints(self, arr):
        # code here
        n = len(arr)
        if n <= 2:
            return arr
        
        res = [arr[0]]
        
        for i in range(1, n - 1):
            if (arr[i] > arr[i - 1] and arr[i] > arr[i + 1]) or \
               (arr[i] < arr[i - 1] and arr[i] < arr[i + 1]):
                if arr[i] != res[-1]:
                    res.append(arr[i])
        
        if arr[-1] != res[-1]:
            res.append(arr[-1])
        
        return res