class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return
        if root_x < root_y:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind(26)

        for c1, c2 in zip(s1, s2):
            uf.union(ord(c1) - ord('a'), ord(c2) - ord('a'))

        res = []
        for ch in baseStr:
            smallest = chr(uf.find(ord(ch) - ord('a')) + ord('a'))
            res.append(smallest)

        return ''.join(res)