class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        for o in operations:
            if o == "C":
                total -= stack.pop()
                continue
            
            n = None
            if o == "D":
                n = stack[-1] * 2
            elif o == "+":
                n = stack[-1] + stack[-2]
            else:
                n = int(o)
            total += n
            stack.append(n)
        return total