# BinaryHeapの実装
class BinaryHeap():
    def __init__(self, l):
        l.sort()
        self.a = [[]]
        for i in range(len(l)):
            if len(self.a[-1]) == 2**(len(self.a) - 1):
                self.a.append([])
            self.a[-1].append(l[i])
    
    def add(self, x):
        if len(self.a[-1]) == 2**(len(self.a) - 1):
            self.a.append([])
        self.a[-1].append(x)
        j = len(self.a[-1]) - 1
        for i in range(len(self.a)-1, 0, -1):
            if self.a[i-1][j//2] > self.a[i][j]:
                self.a[i-1][j//2], self.a[i][j] = self.a[i][j], self.a[i-1][j//2]
                j //= 2
            else:
                break
    
    def remove(self):
        ans = self.a[0][0]
        x = self.a[-1].pop(-1)
        if self.a[-1] == []:
            self.a.pop(-1)
            if self.a == []:
                self.a.append([])
                return ans
        self.a[0][0] = x
        j = 0
        for i in range(len(self.a)-2):
            if self.a[i][j] > self.a[i+1][2*j] or self.a[i][j] > self.a[i+1][2*j+1]:
                if self.a[i+1][2*j] < self.a[i+1][2*j+1]:
                    self.a[i][j], self.a[i+1][2*j] = self.a[i+1][2*j], self.a[i][j]
                    j = 2 * j
                else:
                    self.a[i][j], self.a[i+1][2*j+1] = self.a[i+1][2*j+1], self.a[i][j]
                    j = 2 * j + 1
            else:
                return ans
        i = len(self.a)-2
        if 2*j  < len(self.a[-1]):
            if len(self.a[-1]) == 2 * j + 1:
                if self.a[i][j] > self.a[i+1][2*j]:
                    self.a[i][j], self.a[i+1][2*j] = self.a[i+1][2*j], self.a[i][j]
            elif self.a[i][j] > self.a[i+1][2*j] or self.a[i][j] > self.a[i+1][2*j+1]:
                if self.a[i+1][2*j] < self.a[i+1][2*j+1]:
                    self.a[i][j], self.a[i+1][2*j] = self.a[i+1][2*j], self.a[i][j]
                else:
                    self.a[i][j], self.a[i+1][2*j+1] = self.a[i+1][2*j+1], self.a[i][j]
        return ans

    def debug(self):
        return self.a
