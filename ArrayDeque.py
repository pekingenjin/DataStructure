# Dequeの実装(python3)
# 両端に対する操作のみ可能
class ArrayDeque():
    def __init__(self):
        self.l = [0 for _ in range(2)]
        self.start = 0
        self.end = 0

    def resize(self):
        l = [self.l[i] for i in range(self.start, len(self.l))]
        for i in range(self.start):
            l.append(self.l[i])
        for _ in range(len(self.l)):
            l.append(0)
        self.start = 0
        self.end = len(self.l)
        self.l = l
    
    def addright(self, x):
        self.l[self.end] = x
        self.end += 1
        self.end %= len(self.l)
        if self.start == self.end:
            self.resize()
    
    def addleft(self, x):
        self.l[self.start-1] = x
        self.start -= 1
        self.start %= len(self.l)
        if self.start == self.end:
            self.resize()
    
    def removeright(self):
        ans = self.l[self.end-1]
        self.l[self.end-1] = 0
        self.end -= 1
        self.end %= len(self.l)
        return ans

    def removeleft(self):
        ans = self.l[self.start]
        self.l[self.start] = 0
        self.start += 1
        self.start %= len(self.l)
        return ans

    def empty(self):
        return self.start == self.end
