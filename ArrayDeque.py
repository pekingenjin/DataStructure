# Dequeの実装(python3)
# 両端に対する操作のみ実装
class ArrayDeque():
    def __init__(self, l):
        if len(l) == 0:
            self.flag = True
        else:
            self.flag = False
        self.start = 0
        self.end = len(l)
        for _ in range(len(l)):
            l.append(None)
        self.l = l

    def resize(self):
        if self.start == self.end:
            l = [self.l[i] for i in range(self.start, len(self.l))]
            for i in range(self.start):
                l.append(self.l[i])
            for _ in range(len(self.l)):
                l.append(None)
            self.start = 0
            self.end = len(self.l)
            self.l = l
    
    def addright(self, x):
        if self.flag:
            self.l = [x, None]
            self.start = 0
            self.end = 1
            self.flag = False
        else:
            self.resize()
            self.l[self.end] = x
            self.end += 1
            self.end %= len(self.l)
    
    def addleft(self, x):
        if self.flag:
            self.l = [x, None]
            self.start = 0
            self.end = 1
            self.flag = False
        else:
            self.resize()
            self.l[self.start-1] = x
            self.start -= 1
            self.start %= len(self.l)
    
    def removeright(self):
        if self.flag:
            return None
        else:
            x = self.l[self.end-1]
            self.end -= 1
            self.end %= len(self.l)
            if self.start == self.end:
                self.flag = True
            return x

    def removeleft(self):
        if self.flag:
            return None
        else:
            x = self.l[self.start]
            self.start += 1
            self.start %= len(self.l)
            if self.start == self.end:
                self.flag = True
            return x
        
    def origin(self):
        l = []
        if self.flag:
            return l
        elif self.start < self.end:
            for i in range(self.start, self.end):
                l.append(self.l[i])
            return l
        else:
            for i in range(self.start, len(self.l)):
                l.append(self.l[i])
            for i in range(self.end):
                l.append(self.l[i])
            return l

    def get(self, i):
        if self.flag:
            return None
        j = (self.end - self.start) % len(self.l)
        if -j <= i < 0:
            i = i + j
        elif i >= j or i < -j:
            return None
        elif i < len(self.l) - self.start:
                return self.l[i + self.start]
        else:
            return self.l[i + self.start - len(self.l)]

    def empty(self):
        return self.flag
    
    def debug(self):
        return self.l
