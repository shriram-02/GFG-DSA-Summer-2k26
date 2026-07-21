class kStacks:

    def __init__(self, n, k):
        self.stacks = [[] for _ in range(k)]

    def push(self, x, i):
        self.stacks[i].append(x)

    def pop(self, i):
        if self.stacks[i]:
            return self.stacks[i].pop()
        return -1