class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]
        self.rank = [0] * (size + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        n = len(equations)
        uf = UnionFind(26)

        # return ord("a")

        equal = []
        nequal = []

        for s in equations:
            if s[1] == "=":
                equal.append(s)
            else:
                nequal.append(s)
        
        for s in equal:
            uf.union(ord(s[0])-97, ord(s[3])-97)
        
        for s in nequal:
            if uf.connected(ord(s[0])-97, ord(s[3])-97):
                return False
        
        return True
        