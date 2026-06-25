class Solution:
    def findPages(self, arr, k):
        # Code here
        if k > len(arr):
            return -1
            
        def is_possible(mid):
            students = 1
            current_sum = 0
            for pages in arr:
                if current_sum + pages > mid:
                    students += 1
                    current_sum = pages
                    if students > k:
                        return False
                else:
                    current_sum += pages
            return True

        low = max(arr)
        high = sum(arr)
        res = -1
        
        while low <= high:
            mid = (low + high) // 2
            if is_possible(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res