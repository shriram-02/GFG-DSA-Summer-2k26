class Solution:
    def peakElement(self, arr):
        # Code here
        low, high = 0, len(arr) - 1
        
        while low < high:
            mid = (low + high) // 2
            
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid
                
        return low