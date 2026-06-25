class Solution:
    def merge(self, arr, l, m, r):
        # Create temporary copies of the subarrays
        left_sub = arr[l:m+1]
        right_sub = arr[m+1:r+1]
        
        i = j = 0
        k = l
        
        # Merge the temporary arrays back into arr[l..r]
        while i < len(left_sub) and j < len(right_sub):
            if left_sub[i] <= right_sub[j]:
                arr[k] = left_sub[i]
                i += 1
            else:
                arr[k] = right_sub[j]
                j += 1
            k += 1
            
        # Copy remaining elements of left_sub, if any
        while i < len(left_sub):
            arr[k] = left_sub[i]
            i += 1
            k += 1
            
        # Copy remaining elements of right_sub, if any
        while j < len(right_sub):
            arr[k] = right_sub[j]
            j += 1
            k += 1

    def mergeSort(self, arr, l, r):
        if l < r:
            m = l + (r - l) // 2
            
            # Sort first and second halves
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            
            # Merge sorted halves
            self.merge(arr, l, m, r)