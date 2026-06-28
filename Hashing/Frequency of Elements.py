from collections import Counter

class Solution:
    def countFreq(self, arr):
        freq = Counter(arr)
        ans = []
        
        for x in arr:
            if x in freq:
                ans.append([x, freq[x]])
                del freq[x]
                
        return ans