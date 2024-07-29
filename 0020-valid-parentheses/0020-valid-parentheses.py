class Solution:
    def isValid(self, s: str) -> bool:
        opPar = set(["(", "[", "{"])
        stack = []

        for ch in s:
            if ch in opPar: stack.append(ch)
            elif len(stack) > 0 and (ord(stack[-1]) == ord(ch) - 1 or ord(stack[-1]) == ord(ch) - 2):
                stack.pop()
            else:
                return False
        return len(stack) == 0