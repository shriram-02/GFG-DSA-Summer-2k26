class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        if low < high:
            # pi is partitioning index, arr[p] is now at right place
            pi = self.partition(arr, low, high)
            
            # Separately sort elements before partition and after partition
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)
    
    def partition(self, arr, low, high):
        # Using the last element as the pivot
        pivot = arr[high]
        i = low - 1  # Index of smaller element
        
        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                
        # Swap the pivot element with the element at i + 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1