class Solution:
    def mergeAndCount(self, arr, temp_arr, left, mid, right):
        i = left     # Starting index for left subarray
        j = mid + 1  # Starting index for right subarray
        k = left     # Starting index to be filled in temp_arr
        inv_count = 0

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                # There are mid - i elements left in the left subarray
                # because left subarray is sorted, all these elements will be > arr[j]
                temp_arr[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1

        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1

        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1

        for loop_idx in range(left, right + 1):
            arr[loop_idx] = temp_arr[loop_idx]
            
        return inv_count

    def _mergeSort(self, arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2

            inv_count += self._mergeSort(arr, temp_arr, left, mid)
            inv_count += self._mergeSort(arr, temp_arr, mid + 1, right)
            inv_count += self.mergeAndCount(arr, temp_arr, left, mid, right)
            
        return inv_count

    def inversionCount(self, arr):
        n = len(arr)
        temp_arr = [0] * n
        return self._mergeSort(arr, temp_arr, 0, n - 1)