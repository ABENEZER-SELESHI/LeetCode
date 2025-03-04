class Node:
    def __init__(self, val:str, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        self.dummy = Node(homepage)
        self.indexer = self.dummy


        

    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.indexer.next = new_node
        new_node.prev = self.indexer
        self.indexer = self.indexer.next

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.indexer.prev:
                self.indexer = self.indexer.prev
        return self.indexer.val
        

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.indexer.next:
                self.indexer = self.indexer.next
        return self.indexer.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)