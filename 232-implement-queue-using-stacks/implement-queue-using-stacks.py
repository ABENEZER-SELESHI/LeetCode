class MyQueue:

    def __init__(self):
        self.forward_stack = []
        self.backward_stack = []
        

    def push(self, x: int) -> None:
        if self.backward_stack:
            while self.backward_stack:
                self.forward_stack.append(self.backward_stack.pop())
        self.forward_stack.append(x)
        

    def pop(self) -> int:
        if not self.backward_stack:
            while self.forward_stack:
                self.backward_stack.append(self.forward_stack.pop())
        if not self.empty():
            # print(self.backward_stack)
            return self.backward_stack.pop()
        

    def peek(self) -> int:
        if self.backward_stack:
            return self.backward_stack[-1]
        elif self.forward_stack:
            return self.forward_stack[0]
        

    def empty(self) -> bool:
        if len(self.forward_stack) == len(self.backward_stack):
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()