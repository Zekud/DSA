class ListNode:
    def __init__(self,val):
        self.prev = None
        self.val = val
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = ListNode(homepage)
        
    def visit(self, url: str) -> None:
        newNode = ListNode(url)
        self.current.next = newNode
        newNode.prev = self.current
        self.current = newNode

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.prev:
                self.current = self.current.prev
        return self.current.val
        

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.next:
                self.current = self.current.next
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)