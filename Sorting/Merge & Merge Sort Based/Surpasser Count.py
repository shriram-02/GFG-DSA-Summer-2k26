class Solution:
    def merge(self, arr, indices, surpasser_counts, left, mid, right):
        temp_indices = [0] * (right - left + 1)
        i = left
        j = mid + 1
        k = 0
        
        # Count elements from the right subarray that are smaller
        right_seen_smaller = 0
        
        while i <= mid and j <= right:
            # Sort descending to natively compute elements larger to the right
            if arr[indices[i]] > arr[indices[j]]:
                # arr[indices[j]] is smaller than arr[indices[i]], 
                # so it cannot be a surpasser. But elements after it might be.
                temp_indices[k] = indices[i]
                # Elements remaining in the right subarray are smaller than arr[indices[j]], 
                # meaning elements seen so far in right subarray are larger than arr[indices[i]].
                surpasser_counts[indices[i]] += (right - j + 1)
                i += 1
            else:
                temp_indices[k] = indices[j]
                j += 1
            k += 1
            
        while i <= mid:
            temp_indices[k] = indices[i]
            i += 1
            k += 1
            
        while j <= right:
            temp_indices[k] = indices[j]
            j += 1
            k += 1
            
        for loop_idx in range(len(temp_indices)):
            indices[left + loop_idx] = temp_indices[loop_idx]

    def _mergeSort(self, arr, indices, surpasser_counts, left, right):
        if left < right:
            mid = (left + right) // 2
            self._mergeSort(arr, indices, surpasser_counts, left, mid)
            self._mergeSort(arr, indices, surpasser_counts, mid + 1, right)
            self.merge(arr, indices, surpasser_counts, left, mid, right)

    def findSurpassers(self, arr):
        n = len(arr)
        surpasser_counts = [0] * n
        indices = list(range(n))
        
        # Use a modified Merge Sort on indices
        self._mergeSort(arr, indices, surpasser_counts, 0, n - 1)
        return surpasser_counts