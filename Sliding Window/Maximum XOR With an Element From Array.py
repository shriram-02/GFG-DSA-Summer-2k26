class TrieNode:
    def __init__(self):
        self.child = [None, None]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if not node.child[bit]:
                node.child[bit] = TrieNode()
            node = node.child[bit]

    def getMaxXor(self, num):
        node = self.root
        ans = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if node.child[1 - bit]:
                ans |= (1 << i)
                node = node.child[1 - bit]
            else:
                node = node.child[bit]
        return ans

class Solution:
    def maxXor(self, arr, queries):
        arr.sort()
        q = []
        for i, (x, m) in enumerate(queries):
            q.append((m, x, i))
        q.sort()

        trie = Trie()
        ans = [-1] * len(queries)
        j = 0

        for m, x, idx in q:
            while j < len(arr) and arr[j] <= m:
                trie.insert(arr[j])
                j += 1
            if j > 0:
                ans[idx] = trie.getMaxXor(x)

        return ans