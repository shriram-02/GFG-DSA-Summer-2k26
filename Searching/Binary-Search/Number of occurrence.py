class Solution:
    def countFreq(self, arr, target):
        # code here
        def lower_bound(x):
            low, high = 0, len(arr)
            while low < high:
                mid = (low + high) // 2
                if arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid
            return low
        
        def upper_bound(x):
            low, high = 0, len(arr)
            while low < high:
                mid = (low + high) // 2
                if arr[mid] <= x:
                    low = mid + 1
                else:
                    high = mid
            return low
        
        return upper_bound(target) - lower_bound(target)