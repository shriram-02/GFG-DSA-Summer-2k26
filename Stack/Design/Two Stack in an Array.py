class TwoStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push1(self, x):
        self.s1.append(x)

    def push2(self, x):
        self.s2.append(x)

    def pop1(self):
        if self.s1:
            return self.s1.pop()
        return -1

    def pop2(self):
        if self.s2:
            return self.s2.pop()
        return -1