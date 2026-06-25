class Solution:
    def findMoves(self, chairs, passengers):
        # Sorting both puts the closest pairs into aligned index matching
        chairs.sort()
        passengers.sort()
        
        total_moves = 0
        for c, p in zip(chairs, passengers):
            total_moves += abs(c - p)
            
        return total_moves