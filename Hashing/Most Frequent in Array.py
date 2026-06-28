from collections import Counter

class Solution:
    def mostFreqEle(self, arr):
        freq = Counter(arr)
        max_freq = max(freq.values())
        
        ans = float('-inf')
        for num, cnt in freq.items():
            if cnt == max_freq:
                ans = max(ans, num)
                
        return ans