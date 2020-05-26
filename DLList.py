# DLListの実装
class DLList():
    def __init__(self, l):
        l.insert(0, 'dummy')
        self.l = l
        self.length = len(l) - 1 # 本来の配列の長さ
        self.next = [i+1 for i in range(len(l))]
        self.next[-1] = 0
        self.prev = [i-1 for i in range(len(l))]
        self.prev[0] = len(l) - 1
        self.debris = [] # 使わなくなった場所

    def search(self, i):
        if i >= self.length or i < -self.length:
            return None
        i %= self.length
        if i < self.length // 2:
            j = self.next[0]
            for _ in range(i):
                j = self.next[j]
        else:
            j = 0
            for _ in range(self.length - i):
                j = self.prev[j]
        return j

    def get(self, i):
        return self.l[self.search(i)]

    def insert(self, i, x):
        if len(self.debris) == 0:
            self.debris.append(len(self.l))
            self.l.append(None)
            self.next.append(None)
            self.prev.append(None)
        j = self.debris.pop(-1)
        k = self.search(i)
        self.l[j] = x
        self.next[j] = k
        self.prev[j] = self.prev[k]
        self.next[self.prev[k]] = j
        self.prev[k] = j
        self.length += 1
    
    def remove(self, i):
        j = self.search(i)
        self.next[self.prev[j]] = self.next[j]
        self.prev[self.next[j]] = self.prev[j]
        self.debris.append(j)
        self.length -= 1
        return self.l[j]

    def origin(self):
        l = []
        j = 0
        for _ in range(self.length):
            j = self.next[j]
            l.append(self.l[j])
        return l

    def debug(self):
        return self.l
