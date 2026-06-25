class Solution:
    def aggressiveCows(self, stalls, k):
        # Code here
        stalls.sort()
        
        def can_place(distance):
            count = 1
            last_pos = stalls[0]
            for i in range(1, len(stalls)):
                if stalls[i] - last_pos >= distance:
                    count += 1
                    last_pos = stalls[i]
                    if count >= k:
                        return True
            return False

        low = 1
        high = stalls[-1] - stalls[0]
        res = 0
        
        while low <= high:
            mid = (low + high) // 2
            if can_place(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res