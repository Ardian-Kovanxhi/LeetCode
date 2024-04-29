class BrowserHistory:

    def __init__(self, homepage: str):
        self.hisArr = [homepage]
        self.currInd = -1

    def visit(self, url: str) -> None:
        if self.currInd < -1:
            self.hisArr = self.hisArr[:self.currInd + 1]
        self.hisArr.append(url)
        self.currInd = -1

    def back(self, steps: int) -> str:
        negLen = len(self.hisArr) * -1
        self.currInd -= steps
        if self.currInd < negLen: self.currInd = negLen
        return self.hisArr[self.currInd]
        

    def forward(self, steps: int) -> str:
        self.currInd += steps
        if self.currInd > -1: self.currInd = -1
        return self.hisArr[self.currInd]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)