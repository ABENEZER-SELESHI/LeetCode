class RecentCounter:

    def __init__(self):
        self.que = []
        self.left = 0
        

    def ping(self, t: int) -> int:
        self.que.append(t)
        
        while (t - 3000) > self.que[self.left]:
            self.left += 1
        
        return len(self.que) - self.left
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)