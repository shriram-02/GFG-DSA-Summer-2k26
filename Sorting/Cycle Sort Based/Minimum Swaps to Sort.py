class Solution:
    # Function to find the minimum number of swaps required to sort the array.
    def minSwaps(self, arr):
        n = len(arr)
        
        # Store elements along with their original indices
        arr_pos = [*enumerate(arr)]
        
        # Sort the elements based on their values
        arr_pos.sort(key=lambda x: x[1])
        
        # To keep track of visited elements
        visited = [False] * n
        ans = 0
        
        for i in range(n):
            # If element is already visited or it's already in the correct position
            if visited[i] or arr_pos[i][0] == i:
                continue
                
            # Find the number of nodes in this cycle
            cycle_size = 0
            j = i
            
            while not visited[j]:
                visited[j] = True
                # Move to the next node in the cycle
                j = arr_pos[j][0]
                cycle_size += 1
                
            # Update answer by adding current cycle's swaps
            if cycle_size > 0:
                ans += (cycle_size - 1)
                
        return ans