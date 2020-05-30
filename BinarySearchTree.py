# BinarySearchTreeの実装
class BinarySearchTree():
    def __init__(self):
        # left, right, parent, root, debrisはdataのindexを格納
        self.data = []
        self.left = []
        self.right = []
        self.parent = []
        self.root = None
        self.debris = []

    # xが見つかればxのindex、見つからなければ探索した最後のnodeのindexを返す
    def find(self, x):
        i = self.root
        while True:
            if self.data[i] == x:
                return i
            elif self.data[i] < x:
                if self.right[i] == None:
                    return i
                else:
                    i = self.right[i]
            elif self.left[i] == None:
                return i
            else:
                i = self.left[i]
    
    # 追加する場所のindexを返す
    def next_place(self):
        if self.debris == []:
            self.data.append(None)
            self.left.append(None)
            self.right.append(None)
            self.parent.append(None)
            return len(self.data) - 1
        else:
            return self.debris.pop(-1)

    def add(self, x):
        if self.root == None:
            self.data = [x]
            self.left = [None]
            self.right = [None]
            self.parent = [None]
            self.root = 0
            self.debris = []
        else:
            p = self.find(x) # p = (xの親となるindex)
            if self.data[p] != x:
                i = self.next_place()
                self.data[i] = x
                self.parent[i] = p
                if self.data[p] < x:
                    self.right[p] = i
                else:
                    self.left[p] = i
    
    def remove(self, x):
        if self.root == None:
            return None
        i = self.find(x)
        if self.data[i] == x:

            # parent[j]をparent[i]に変更
            if self.left[i] == None and self.right[i] == None:
                j = None
            elif self.left[i] == None:
                j = self.right[i]
                self.parent[j] = self.parent[i]
            elif self.right[i] == None:
                j = self.left[i]
                self.parent[j] = self.parent[i]
            elif self.left[self.right[i]] == None:
                j = self.right[i]
                self.parent[j] = self.parent[i]
                self.left[j] = self.left[i]
                self.parent[self.left[i]] = j
            elif self.right[self.left[i]] == None:
                j = self.left[i]
                self.parent[j] = self.parent[i]
                self.right[j] = self.right[i]
                self.parent[self.right[i]] = j
            else:
                j = self.right[i]
                while self.left[j] != None:
                    j = self.left[j]
                self.left[self.parent[j]] = self.right[j]
                if self.right[j] != None:
                    self.parent[self.right[j]] = self.parent[j]
                self.parent[j] = self.parent[i]
                self.left[j] = self.left[i]
                self.right[j] = self.right[i]
                self.parent[self.left[i]] = j
                self.parent[self.right[i]] = j
                

            # parent[i]の子をjに変更
            if self.root == i:
                self.root = j
            elif self.left[self.parent[i]] == i:
                self.left[self.parent[i]] = j
            else:
                self.right[self.parent[i]] = j
            
            # iの初期化
            self.data[i] = None
            self.left[i] = None
            self.right[i] = None
            self.parent[i] = None
            self.debris.append(i)
    
    def exist(self, x):
        return self.data[self.find(x)] == x

    def empty(self):
        return self.root == None

    def debug(self):
        if self.root == None:
            return 'empty'
        tree = [[self.root]]
        flag = True
        while flag:
            l = []
            for i in tree[-1]:
                if i == '  ':
                    l.append('  ')
                    l.append('  ')
                    continue
                elif self.left[i] == None:
                    l.append('  ')
                else:
                    l.append(self.left[i])
                if self.right[i] == None:
                    l.append('  ')
                else:
                    l.append(self.right[i])
            flag = False
            for i in l:
                if i == '  ':
                    continue
                else:
                    tree.append(l)
                    flag = True
                    break
        for i in range(len(tree)):
            l = []
            for j in tree[i]:
                if j == '  ':
                    l.append(j)
                else:
                    k = str(self.data[j])
                    if len(k) == 1:
                        k = ' ' + k
                    l.append(k)
            n = len(tree) - i
            m = (2**n-1) * '  '
            l = (m.join(l))
            print((2**(n-1)-1) * '  ' + l)
        print()


bst = BinarySearchTree()
l = [7, 3, 1, 5, 4, 6, 11, 9, 8, 13, 12, 14]
for i in l:
    bst.add(i)
bst.debug()
