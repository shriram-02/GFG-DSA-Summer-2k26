from collections import deque

class myStack:
    
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        if self.q:
            self.q.popleft()

    def top(self):
        if self.q:
            return self.q[0]
        return -1

    def size(self):
        return len(self.q)