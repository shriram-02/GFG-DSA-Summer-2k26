class Solution:
    def single(self, arr):
        # code here
        n = len(arr)
        
        if n == 1:
            return arr[0]
        if arr[0] != arr[1]:
            return arr[0]
        if arr[n - 1] != arr[n - 2]:
            return arr[n - 1]
        
        low, high = 1, n - 2
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] != arr[mid - 1] and arr[mid] != arr[mid + 1]:
                return arr[mid]
            
            if (mid % 2 == 0 and arr[mid] == arr[mid + 1]) or \
               (mid % 2 == 1 and arr[mid] == arr[mid - 1]):
                low = mid + 1
            else:
                high = mid - 1