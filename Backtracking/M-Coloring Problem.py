class Solution:
    def graphColoring(self, v, edges, m):
        graph = [[] for _ in range(v)]

        for u, w in edges:
            graph[u].append(w)
            graph[w].append(u)

        color = [0] * v

        def safe(node, c):
            for nei in graph[node]:
                if color[nei] == c:
                    return False
            return True

        def dfs(node):
            if node == v:
                return True

            for c in range(1, m + 1):
                if safe(node, c):
                    color[node] = c
                    if dfs(node + 1):
                        return True
                    color[node] = 0

            return False

        return dfs(0)