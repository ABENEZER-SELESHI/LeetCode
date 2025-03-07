class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k
        self.value = value
        self.que = deque()
        self.count = 0
        

    def consec(self, num: int) -> bool:
        if len(self.que) < self.k:
            self.que.append(num)
            if num == self.value:
                self.count += 1
        else:
            self.que.append(num)
            if num == self.value:
                self.count += 1
            x = self.que.popleft()
            if x == self.value:
                self.count -= 1
        if self.count == self.k:
            return True
        else:
            return False
        # return self.que
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)