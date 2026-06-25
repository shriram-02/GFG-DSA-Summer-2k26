class Solution:
    # Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr):
        n = len(arr)
        
        # Rearrange elements to their correct bucket/index positions
        for i in range(n):
            while 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:
                # Swap elements to place arr[i] at index arr[i] - 1
                correct_idx = arr[i] - 1
                arr[i], arr[correct_idx] = arr[correct_idx], arr[i]
                
        # Find the first index where the correct number is missing
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1
                
        # If all numbers from 1 to n are present
        return n + 1