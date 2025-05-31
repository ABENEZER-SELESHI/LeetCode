class UnionFind:
    def __init__(self):
        self.parent = {}
        self.weight = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.weight[x] = 1.0
        if self.parent[x] != x:
            orig_parent = self.parent[x]
            self.parent[x] = self.find(orig_parent)
            self.weight[x] *= self.weight[orig_parent]
        return self.parent[x]

    def union(self, x, y, value):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.parent[root_x] = root_y
            self.weight[root_x] = value * self.weight[y] / self.weight[x]

    def isConnected(self, x, y):
        return x in self.parent and y in self.parent and self.find(x) == self.find(y)

    def divide(self, x, y):
        if not self.isConnected(x, y):
            return -1.0
        return self.weight[x] / self.weight[y]
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = UnionFind()

        for (a, b), value in zip(equations, values):
            uf.union(a, b, value)

        res = []
        for a, b in queries:
            res.append(uf.divide(a, b))
        return res
        