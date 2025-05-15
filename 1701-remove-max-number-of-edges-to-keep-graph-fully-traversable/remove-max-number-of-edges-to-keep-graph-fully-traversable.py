class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]
        self.red_parent = [i for i in range(size + 1)] 
        self.green_parent = [i for i in range(size + 1)] 
        self.rank = [0] * (size + 1)
        self.red_rank = [0] * (size + 1)
        self.green_rank = [0] * (size + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]
    def red_find(self, x):
        if self.red_parent[x] != x:
            self.red_parent[x] = self.red_find(self.red_parent[x])  # path compression
        return self.red_parent[x]
    def green_find(self, x):
        if self.green_parent[x] != x:
            self.green_parent[x] = self.green_find(self.green_parent[x])  # path compression
        return self.green_parent[x]

    def union(self, x, y): # z = (x, y)
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
                self.red_parent[root_x] = root_y
                self.green_parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
                self.red_parent[root_y] = root_x
                self.green_parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.red_parent[root_y] = root_x
                self.green_parent[root_y] = root_x
                self.rank[root_x] += 1
                self.red_rank[root_x] += 1
                self.green_rank[root_x] += 1
    def red_union(self, x, y): # z = (x, y)
        root_x = self.red_find(x)
        root_y = self.red_find(y)

        if root_x != root_y:
            if self.red_rank[root_x] < self.red_rank[root_y]:
                self.red_parent[root_x] = root_y
            elif self.red_rank[root_x] > self.red_rank[root_y]:
                self.red_parent[root_y] = root_x
            else:
                self.red_parent[root_y] = root_x
                self.red_rank[root_x] += 1
    def green_union(self, x, y): # z = (x, y)
        root_x = self.green_find(x)
        root_y = self.green_find(y)

        if root_x != root_y:
            if self.green_rank[root_x] < self.green_rank[root_y]:
                self.green_parent[root_x] = root_y
            elif self.green_rank[root_x] > self.green_rank[root_y]:
                self.green_parent[root_y] = root_x
            else:
                self.green_parent[root_y] = root_x
                self.green_rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    def red_connected(self, x, y):
        return self.red_find(x) == self.red_find(y)
    def green_connected(self, x, y):
        return self.green_find(x) == self.green_find(y)
    

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        tracker = []
        count = 0
        for x, y, z in edges:
            if uf.connected(y, z):
                count += 1
                continue
            if x == 3:
                uf.union(y, z)
            else:
                tracker.append([x, y, z])
        
        for x, y, z in tracker:
            if x == 1:
                if uf.red_connected(y, z):
                    count += 1
                uf.red_union(y, z)
            else:
                if uf.green_connected(y, z):
                    count += 1
                uf.green_union(y, z)
        x = 1
        for i in range(2, n + 1):
            if not (uf.red_connected(x, i) and uf.green_connected(x, i)):
                return -1
        
        return count
        
        