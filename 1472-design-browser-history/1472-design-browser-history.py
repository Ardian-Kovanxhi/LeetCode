class ListNode:
    def __init__(self, val, prevVal, nextVal):
        self.val = val
        self.prev = prevVal
        self.next = nextVal

class BrowserHistory:

    def __init__(self, homepage: str):
        self.page = ListNode(homepage, None, None)
        

    def visit(self, url: str) -> None:
        temp = ListNode(url, self.page, None)
        self.page.next = temp
        self.page = temp
        return

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.page.prev == None: break
            self.page = self.page.prev
        return self.page.val

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.page.next == None: break
            self.page = self.page.next
        return self.page.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)